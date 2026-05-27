import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from models import User

# ── App setup ────────────────────────────────────────────────────────────────

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{os.path.join(BASE_DIR, 'users.db')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

VALID_ROLES = ["Developer", "Designer", "Manager", "Tester", "DevOps"]

# ── Helpers ───────────────────────────────────────────────────────────────────

def error(message, code):
    return jsonify({"error": message}), code


def validate_user(data, is_update=False):
    """Return a dict of field errors (empty = valid)."""
    errors = {}
    if not is_update or "name" in data:
        if not str(data.get("name", "")).strip():
            errors["name"] = "Name is required."
    if not is_update or "email" in data:
        if not str(data.get("email", "")).strip():
            errors["email"] = "Email is required."
    if not is_update or "role" in data:
        role = data.get("role", "")
        if role not in VALID_ROLES:
            errors["role"] = f"Role must be one of: {', '.join(VALID_ROLES)}."
    return errors


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/users", methods=["GET"])
def get_users():
    search = request.args.get("search", "").strip()
    role   = request.args.get("role",   "").strip()
    page   = request.args.get("page",   1,  type=int)
    limit  = request.args.get("limit",  10, type=int)

    query = User.query

    if role:
        query = query.filter(User.role == role)

    if search:
        like = f"%{search}%"
        query = query.filter(
            User.name.ilike(like)
            | User.email.ilike(like)
            | User.company.ilike(like)
        )

    total      = query.count()
    pagination = query.paginate(page=page, per_page=limit, error_out=False)
    users      = [u.to_dict() for u in pagination.items]

    return jsonify({
        "users":       users,
        "total":       total,
        "page":        page,
        "limit":       limit,
        "total_pages": pagination.pages,
    }), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error(f"User with id {user_id} not found.", 404)
    return jsonify(user.to_dict()), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return error("Request body must be JSON.", 400)

    errs = validate_user(data)
    if errs:
        return jsonify({"errors": errs}), 422

    if User.query.filter(User.email.ilike(data["email"].strip())).first():
        return error("A user with this email already exists.", 409)

    user = User(
        name    = data["name"].strip(),
        email   = data["email"].strip(),
        role    = data["role"].strip(),
        bio     = data.get("bio",     "").strip(),
        company = data.get("company", "").strip(),
        website = data.get("website", "").strip(),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error(f"User with id {user_id} not found.", 404)

    data = request.get_json()
    if not data:
        return error("Request body must be JSON.", 400)

    errs = validate_user(data, is_update=True)
    if errs:
        return jsonify({"errors": errs}), 422

    # Duplicate email check (exclude current user)
    if "email" in data:
        existing = User.query.filter(
            User.email.ilike(data["email"].strip()),
            User.id != user_id
        ).first()
        if existing:
            return error("A user with this email already exists.", 409)

    for field in ("name", "email", "role", "bio", "company", "website"):
        if field in data:
            setattr(user, field, data[field].strip())

    db.session.commit()
    return jsonify(user.to_dict()), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error(f"User with id {user_id} not found.", 404)
    name = user.name
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User '{name}' deleted successfully."}), 200


@app.route("/roles", methods=["GET"])
def get_roles():
    return jsonify(VALID_ROLES), 200


# ── Init & run ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Auto-seed if empty
        if User.query.count() == 0:
            from seed import seed
            seed()
    app.run(debug=True, port=5000)
