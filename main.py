# password validation using a regular expression.

import re

def password_validation():
    i = 0
    while i == 0:
        try:
            pattern = re.compile(r"[a-zA-Z\d!@#$%^&*]{8,}")

            first_password = input("\nEnter a new password \nValid characters are A-Z, a-z, 0-9, $%*!@&#^ : ")
            second_password = input("\nPlease enter your new password again: ")

            check = pattern.fullmatch(first_password)
            if len(first_password) < 8:
                print('Your password is only', len(first_password), "characters. Use 8 or more characters.")

            elif check == None:
                print("Acceptable characters to create a password are: a-z, A-Z, 0-9, $ % * ! @ & # ^.")

            elif first_password != second_password:
                print("The passwords do not match, please try again")

            else:
                i += 1
                print("Your new password has been saved.")
                with open("password_file.txt", mode='a') as output_file:
                    output_file.write(first_password)
                    output_file.write("\n")

        except ValueError:
            print("Only use the following characters: a-z, A-Z, 0-9, $ % * ! @ & # ^")


password_validation()
