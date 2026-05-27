from database import db


class User(db.Model):
    __tablename__ = "users"

    id      = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column(db.String(120), nullable=False)
    email   = db.Column(db.String(200), nullable=False, unique=True)
    role    = db.Column(db.String(50),  nullable=False)
    bio     = db.Column(db.Text,        nullable=True, default="")
    company = db.Column(db.String(120), nullable=True, default="")
    website = db.Column(db.String(200), nullable=True, default="")

    def to_dict(self):
        return {
            "id":      self.id,
            "name":    self.name,
            "email":   self.email,
            "role":    self.role,
            "bio":     self.bio    or "",
            "company": self.company or "",
            "website": self.website or "",
        }
