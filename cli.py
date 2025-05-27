from database import session
from models import User
from lib.helpers import print_heading, get_int_input

def create_user():
    print_heading("Create New User")
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")

    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print("A user with that email already exists.")
        return

    new_user = User(username=name, email=email, role="donor")  # assuming default role
    session.add(new_user)
    session.commit()
    print(f" User '{name}' created successfully!")

def main_menu():
    while True:
        print_heading("Online Donation System")
        print("1. Create user")
        print("2. List causes (coming soon)")
        print("3. Make donation (coming soon)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            print(" Feature coming soon: List causes")
        elif choice == "3":
            print(" Feature coming soon: Make donation")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
