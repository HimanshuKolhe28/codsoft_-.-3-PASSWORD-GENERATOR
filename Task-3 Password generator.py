'''
Problem Statement

A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the

password.

Generate Password: Use a combination of random characters to

generate a password of the specified length.

Display the Password: Print the generated password on the screen.
'''

import random  # Import the random module to generate random choices
import string  # Import the string module to access character sets

# Function to generate a password of a given length
def generate_password(length):
    # Define the character set: includes uppercase, lowercase, digits, and punctuation
    char_set = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly selecting 'length' characters from the char_set
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    # Return the generated password
    return password

# Main function to interact with the user and generate the password
def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length for your password: "))
        
        # Check if the length is a positive integer
        if length <= 0:
            # Raise a ValueError if the length is not positive
            raise ValueError("Password length must be a positive integer.")
        
        # Generate the password using the specified length
        password = generate_password(length)
        
        # Display the generated password to the user
        print("Generated password:", password)
    
    except ValueError as e:
        # Handle invalid input (e.g., non-integer input or negative length)
        print("Invalid input:", e)

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # If so, call the main function to execute the script
    main()
