import re

def verifyLogin():
    hard_username = "Elijah"
    un_attempts = 0
    pwd_attempts = 0
    password = "Micho"

    while un_attempts < 3:
        user_username = str(input("What is your username? "))
        verify_user = re.match(hard_username, user_username, re.IGNORECASE)
        if verify_user is not None:
            print("You have been granted access.\n")

            while pwd_attempts < 3:
                user_pwd = str(input("Now enter the password: "))
                verify_pwd = re.match(password, user_pwd, re.IGNORECASE)
                if verify_pwd is not None:
                    print("Password is correct!")
                    break
                else:
                    print("Access denied.")
                    pwd_attempts += 1

            if pwd_attempts == 3:
                print("You have used all your attempts")
                exit()
        else:
            print("Access denied.")
            un_attempts += 1

        if un_attempts == 3:
            print("You have used all your attempts.")


verifyLogin()