def print_heading(text):
    print("\n" + "=" * len(text))
    print(text.upper())
    print("=" * len(text))

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")
