import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    if length < 1:
        return "Password length must be at least 1."

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character pools
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 1): "))
            if length < 1:
                print("Please enter a valid length (minimum 1).")
                continue
            
            generated_password = generate_password(length)
            print(f"Generated Password: {generated_password}")

            play_again = input("Do you want to generate another password? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for using the Password Generator!")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()