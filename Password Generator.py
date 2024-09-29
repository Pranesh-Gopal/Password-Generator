import random
import string

# Function to generate the password
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    char_pool = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Main function for user input and password generation
def main():
    print("Welcome to the Secure Password Generator!")
    
    # Get user preferences
    try:
        length = int(input("Enter the desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"\nGenerated password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter valid data.")

# Run the program
if __name__ == "__main__":
    main()
