import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Create a password by picking random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
