from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_users = [
    {
        "email": "alice@example.com",
        "hashed_password": "alicepassword123notreallyhashed",
        "items": [
            {"title": "Grocery list", "description": "Milk, eggs, bread"},
            {"title": "Read FastAPI docs", "description": "Finish the SQL databases tutorial"},
        ],
    },
    {
        "email": "bob@example.com",
        "hashed_password": "bobpassword456notreallyhashed",
        "items": [
            {"title": "Fix bug #42", "description": "NullPointerException in checkout flow"},
        ],
    },
    {
        "email": "carol@example.com",
        "hashed_password": "carolpassword789notreallyhashed",
        "items": [],
    },
]

for user_data in sample_users:
    existing = db.query(models.User).filter(models.User.email == user_data["email"]).first()
    if existing:
        continue
    user = models.User(
        email=user_data["email"],
        hashed_password=user_data["hashed_password"],
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    for item_data in user_data["items"]:
        item = models.Item(**item_data, owner_id=user.id)
        db.add(item)
    db.commit()

db.close()
print("Seeded sample users and items into test.db")
