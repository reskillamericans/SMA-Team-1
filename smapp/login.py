from getpass import getpass
import os

user_db_path = "data/user_record/"


def read(email):
    is_valid_email = does_email_exist(email)

    try:
        if is_valid_email:
            f = open(user_db_path + str(email) + ".txt", "r")

        else:
            f = open(user_db_path + email, "r")

    except FileNotFoundError:
        print("User not found")

    except FileExistsError:
        print("User does not exist")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()

    return False


def does_email_exist(email):

    all_users = os.listdir(user_db_path)
    
    for user in all_users:
    
        if user == str(email) + ".txt":
            return True
    
    return False

def authenticated_user(email, password):
    
    if does_email_exist(email):
        user = str.split(read(email), ',')
    
        if password == user[0]:
            return user
    
    return False


def login():
    print('LOGIN')

    email_from_user = input("What is your email? \n")

    is_valid_email = does_email_exist(
        email_from_user
        )

    if is_valid_email:
        password = getpass("What is your password \n")

        user = authenticated_user(
            email_from_user, password)
        if user:
            print("Login was successful.")
            
login()