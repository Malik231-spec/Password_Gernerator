import random
import string

def generate_password(length):
    # Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = upper + lower + digits + symbols

    # Ensure password contains at least one of each
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle password
    random.shuffle(password)

    return ''.join(password)


print("Create Strong Passwords According to Your Need")

while True:
    user_input = input("Enter length or Q for quit: ")

    # Quit condition
    if user_input.lower() == "q":
        print("Thanks for using me.")
        print("Created by Malik Izzat Baig")
        break

    # Check if input is a number
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    password_length = int(user_input)

    # Minimum length check
    if password_length < 4:
        print("Password length must be at least 4.")
        continue

    password = generate_password(password_length)

    print(f"Generated Password: {password}\n")