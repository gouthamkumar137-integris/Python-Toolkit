import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Pool of characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each type
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length randomly
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to make it completely unpredictable
    random.shuffle(password)
    
    return "".join(password)

# Run the generator
if __name__ == "__main__":
    try:
        user_length = int(input("How many characters long should your password be? "))
        print(f"Your secure password: {generate_password(user_length)}")
    except ValueError:
        print("Please enter a valid number.")