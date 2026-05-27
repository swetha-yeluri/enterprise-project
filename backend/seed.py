from app import app
from database import db
from models import User


SEED_USERS = [
    {
        "name": "Alice Johnson",
        "email": "alice@techcorp.io",
        "role": "Developer",
        "bio": "Full-stack developer with 5 years of experience in React and Python.",
        "company": "TechCorp",
        "website": "https://alicejohnson.dev",
    },
    {
        "name": "Bob Martinez",
        "email": "bob@designstudio.co",
        "role": "Designer",
        "bio": "UI/UX designer specializing in design systems and accessible interfaces.",
        "company": "Design Studio",
        "website": "https://bobmartinez.design",
    },
    {
        "name": "Carol Smith",
        "email": "carol@nexustech.com",
        "role": "Manager",
        "bio": "Engineering manager with 8 years of leading cross-functional teams.",
        "company": "Nexus Tech",
        "website": "https://carolsmith.io",
    },
    {
        "name": "David Lee",
        "email": "david@qaexperts.net",
        "role": "Tester",
        "bio": "QA engineer passionate about automated testing and performance benchmarking.",
        "company": "QA Experts",
        "website": "https://davidlee.qa",
    },
    {
        "name": "Eva Chen",
        "email": "eva@cloudops.io",
        "role": "DevOps",
        "bio": "DevOps engineer with expertise in CI/CD pipelines and Kubernetes.",
        "company": "CloudOps",
        "website": "https://evachen.cloud",
    },
    {
        "name": "Frank Wilson",
        "email": "frank@techcorp.io",
        "role": "Developer",
        "bio": "Backend developer specializing in Python microservices and REST APIs.",
        "company": "TechCorp",
        "website": "https://frankwilson.dev",
    },
]


def seed():
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            for data in SEED_USERS:
                db.session.add(User(**data))
            db.session.commit()
            print(f"✅ Seeded {len(SEED_USERS)} users into the database.")
        else:
            print("ℹ️  Database already has users — skipping seed.")


if __name__ == "__main__":
    seed()
