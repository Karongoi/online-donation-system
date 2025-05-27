from database import Base, engine
from cli import main_menu
from models import User, Cause, Donation

if __name__ == "__main__":
    # Create tables in the database
    Base.metadata.create_all(engine)
    main_menu()
