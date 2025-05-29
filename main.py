# main.py

from database import SessionLocal
from models.donor import Donor
from models.organiser import Organiser
from models.cause import Cause
from models.donation import Donation


def register_user(session, user_type):
    print(f"\nRegister as {user_type.capitalize()}:")
    username = input("Enter username: ")
    email = input("Enter email: ")

    if user_type == "donor":
        existing = session.query(Donor).filter(Donor.email == email).first()
        if existing:
            print("Email already registered as donor.")
            return None
        user = Donor(username=username, email=email, balance=1000) 
    else:  
        existing = session.query(Organiser).filter(Organiser.email == email).first()
        if existing:
            print("Email already registered as organizer.")
            return None
        user = Organiser(username=username, email=email)

    session.add(user)
    session.commit()
    print(f"Registration successful. Welcome, {username}!")
    return user


def login():
    print("Login as:")
    print("1. Donor")
    print("2. Organizer")
    choice = input("Select 1 or 2: ")
    session = SessionLocal()

    if choice == '1':
        email = input("Enter donor email: ")
        donor = session.query(Donor).filter(Donor.email == email).first()
        if donor:
            print(f"Welcome back, {donor.username}!")
            donor_menu(donor, session)
        else:
            print("Donor not found.")
            if input("Do you want to register as a new donor? (y/n): ").lower() == 'y':
                donor = register_user(session, "donor")
                if donor:
                    donor_menu(donor, session)

    elif choice == '2':
        email = input("Enter organizer email: ")
        organiser = session.query(Organiser).filter(Organiser.email == email).first()
        if organiser:
            print(f"Welcome back, {organiser.username}!")
            organiser_menu(organiser, session)
        else:
            print("Organizer not found.")
            if input("Do you want to register as a new organizer? (y/n): ").lower() == 'y':
                organiser = register_user(session, "organiser")
                if organiser:
                    organiser_menu(organiser, session)
    else:
        print("Invalid choice.")
    session.close()


def organiser_menu(user, session):
    while True:
        print("\nOrganizer Menu:")
        print("1. Create cause")
        print("2. Add donor")
        print("3. Update donor")
        print("4. Update cause")
        print("5. Delete donor or cause")
        print("6. Sign out")

        choice = input("Select an option: ")

        if choice == '1':
            create_cause(session, user)  
        elif choice == '2':
            add_donor(session)
        elif choice == '3':
            update_donor(session)
        elif choice == '4':
            update_cause(session)
        elif choice == '5':
            delete_donor_or_cause(session)
        elif choice == '6':
            print("Signing out...")
            break
        else:
            print("Invalid option, try again.")


def create_cause(session, organiser):
    print("\n--- Create Cause ---")
    title = input("Cause title: ")
    description = input("Cause description: ")
    try:
        target_amount = float(input("Target amount: "))
    except ValueError:
        print("Invalid target amount.")
        return

    cause = Cause(
        title=title,
        description=description,
        target_amount=target_amount,
        collected_amount=0,
        organiser_id=organiser.id  
    )
    session.add(cause)
    session.commit()
    print(f"Cause '{title}' created successfully.")


def add_donor(session):
    print("\n--- Add Donor ---")
    username = input("Donor username: ")
    email = input("Donor email: ")
    try:
        balance = float(input("Initial balance: "))
    except ValueError:
        print("Invalid balance.")
        return

    existing = session.query(Donor).filter(Donor.email == email).first()
    if existing:
        print("Donor email already exists.")
        return
    donor = Donor(username=username, email=email, balance=balance)
    session.add(donor)
    session.commit()
    print(f"Donor '{username}' added successfully.")


def update_donor(session):
    print("\n--- Update Donor ---")
    email = input("Enter donor email to update: ")
    donor = session.query(Donor).filter(Donor.email == email).first()
    if not donor:
        print("Donor not found.")
        return
    new_username = input(f"New username (current: {donor.username}): ")
    new_balance = input(f"New balance (current: {donor.balance}): ")
    if new_username.strip():
        donor.username = new_username
    if new_balance.strip():
        try:
            donor.balance = float(new_balance)
        except ValueError:
            print("Invalid balance input, skipped.")
    session.commit()
    print("Donor updated successfully.")


def update_cause(session):
    print("\n--- Update Cause ---")
    causes = session.query(Cause).all()
    if not causes:
        print("No causes found.")
        return
    for c in causes:
        print(f"{c.id}. {c.title} (Collected: {c.collected_amount} / Target: {c.target_amount})")
    try:
        cause_id = int(input("Enter cause ID to update: "))
    except ValueError:
        print("Invalid input.")
        return
    cause = session.query(Cause).filter(Cause.id == cause_id).first()
    if not cause:
        print("Cause not found.")
        return
    new_title = input(f"New title (current: {cause.title}): ")
    new_description = input(f"New description (current: {cause.description}): ")
    new_target = input(f"New target amount (current: {cause.target_amount}): ")

    if new_title.strip():
        cause.title = new_title
    if new_description.strip():
        cause.description = new_description
    if new_target.strip():
        try:
            cause.target_amount = float(new_target)
        except ValueError:
            print("Invalid target amount input, skipped.")
    session.commit()
    print("Cause updated successfully.")


def delete_donor_or_cause(session):
    print("\n--- Delete Donor or Cause ---")
    print("1. Delete Donor")
    print("2. Delete Cause")
    choice = input("Select 1 or 2: ")
    if choice == '1':
        email = input("Enter donor email to delete: ")
        donor = session.query(Donor).filter(Donor.email == email).first()
        if donor:
            session.delete(donor)
            session.commit()
            print("Donor deleted.")
        else:
            print("Donor not found.")
    elif choice == '2':
        causes = session.query(Cause).all()
        if not causes:
            print("No causes to delete.")
            return
        for c in causes:
            print(f"{c.id}. {c.title}")
        try:
            cause_id = int(input("Enter cause ID to delete: "))
        except ValueError:
            print("Invalid input.")
            return
        cause = session.query(Cause).filter(Cause.id == cause_id).first()
        if cause:
            session.delete(cause)
            session.commit()
            print("Cause deleted.")
        else:
            print("Cause not found.")
    else:
        print("Invalid choice.")



def donor_menu(user, session):
    while True:
        print("\nDonor Menu:")
        print("1. View causes")
        print("2. Select cause")
        print("3. Donate")
        print("4. Sign out")

        choice = input("Select an option: ")

        if choice == '1':
            view_causes(session)
        elif choice == '2':
            select_cause(session)
        elif choice == '3':
            donate(user, session)
        elif choice == '4':
            print("Signing out...")
            break
        else:
            print("Invalid option, try again.")


def view_causes(session):
    print("\n--- Available Causes ---")
    causes = session.query(Cause).all()
    if not causes:
        print("No causes available.")
        return
    for c in causes:
        print(f"{c.id}. {c.title} - {c.description} (Collected: {c.collected_amount} / Target: {c.target_amount})")


def select_cause(session):
    view_causes(session)
    try:
        cause_id = int(input("Enter cause ID to select: "))
    except ValueError:
        print("Invalid input.")
        return
    cause = session.query(Cause).filter(Cause.id == cause_id).first()
    if cause:
        print(f"Selected Cause: {cause.title} - {cause.description}")
    else:
        print("Cause not found.")


def donate(user, session):
    print("\n--- Donate ---")
    view_causes(session)
    try:
        cause_id = int(input("Enter cause ID to donate to: "))
    except ValueError:
        print("Invalid input.")
        return
    cause = session.query(Cause).filter(Cause.id == cause_id).first()
    if not cause:
        print("Cause not found.")
        return

    try:
        amount = float(input(f"Enter donation amount (Your balance: {user.balance}): "))
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Donation must be positive.")
        return
    if amount > user.balance:
        print("Insufficient balance.")
        return

    
    donation = Donation(donor_id=user.id, cause_id=cause.id, amount=amount)
    session.add(donation)

    
    user.balance -= amount
    
    cause.collected_amount += amount

    session.commit()
    print(f"Thank you for your donation of {amount} to '{cause.title}'!")
    print(f"Your new balance is {user.balance}.")


def main():
    print("Welcome to the Online Donation System CLI")

    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            login()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
