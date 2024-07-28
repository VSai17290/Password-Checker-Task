import string
import getpass

def check_pwd():
    # Prompt the user to enter their password securely
    password = getpass.getpass("Enter Password: ")
    strength = 0  # Initialize the strength counter
    remarks = ''  # Initialize the remarks string
    # Initialize counters for different types of characters
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    # Iterate over each character in the password
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1  # Increment the lowercase character counter
        elif char in string.ascii_uppercase:
            upper_count += 1  # Increment the uppercase character counter
        elif char in string.digits:
            num_count += 1  # Increment the numeric character counter
        elif char == ' ':
            wspace_count += 1  # Increment the whitespace character counter
        else:
            special_count += 1  # Increment the special character counter

    # Evaluate the password strength based on the presence of different character types
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # Determine the strength of the password and assign a corresponding remark
    if strength == 1:
        remarks = "Very Bad Password! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password! Change ASAP"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    # Print the password analysis results
    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    # Print the password strength and hint
    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd=False):
    # Initialize the validity flag
    valid = False
    # Prompt the user based on whether it's the first password check or a subsequent one
    if another_pwd:
        choice = input('Do you want to enter another password (y/n): ')
    else:
        choice = input('Do you want to check password (y/n): ')

    # Validate the user's choice
    while not valid:
        if choice.lower() == 'y':
            return True  # Return True to indicate the user wants to enter another password
        elif choice.lower() == 'n':
            return False  # Return False to indicate the user does not want to enter another password
        else:
            # Prompt the user again if the input was invalid
            print('Invalid, Try Again')
            choice = input('Do you want to check password (y/n): ')

if __name__ == '__main__':
    print('Welcome to Password Checker')
    # Ask the user if they want to check a password
    ask_pw = ask_pwd()
    while ask_pw:
        check_pwd()  # Check the password
        ask_pw = ask_pwd(True)  # Ask if the user wants to check another password
