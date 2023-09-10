import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_special=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Cannot generate password with no character options"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_special)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
