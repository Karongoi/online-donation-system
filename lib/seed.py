from database import session
from models import User, Cause, Donation
from datetime import datetime, timedelta

def seed_data():
    alice = User(username="alice", email="alice@example.com", role="organizer")
    bob = User(username="bob", email="bob@example.com", role="donor")

    cause = Cause(
        title="Save the Forest",
        description="Protect the Amazon rainforest.",
        goal_amount=10000,
        deadline=datetime.now() + timedelta(days=30),
        organiser=alice
    )

    donation = Donation(user=bob, cause=cause, amount=50)

    session.add_all([alice, bob, cause, donation])
    session.commit()
    print(" Seed data added!")

# You can run this file directly to seed your DB
if __name__ == "__main__":
    seed_data()
