from user_sign_up import check, check_username
from user_login_signup_handling import EmailValidator
from show_user_profile import profile
from user_login_signup_handling import SignUp

# this is just the page for logging in
# returning user - checks system return profile if valid
# new user - checks for valid entries and when finally valid, adds to database and returns username and email


def get_current_user_name():
    try:
        print("Sign in ")
        current_user_name = input("Username: ")
        email_check = EmailValidator(current_user_name)
        if email_check.validate_email():
            profile(current_user_name)
    except:
        return "Invalid input"


def new_user():
    print("\nSign up ")
    print("User names cannot exceed length of 20 characters."
          "\nBoth user name and emails are case sensitive.")

    new_user_name = input("Create Username: ")
    while not check_username(new_user_name):
        print("Usernames cannot begin with a numeric character or exceed length of 20 characters")
        new_user_name = input("Create Username: ")
        check_username(new_user_name)
    (hi(new_user_name))


def hi(new_user_name):
    hiya= SignUp(new_user_name)
    hiya.execute_query()


def welcome():
    try:
        print("Hello Welcome to Thirst Trap!")
        user_status = input("Please choose one of the following: Returning User or New User: ").lower()
        if user_status == 'returning user':
            get_current_user_name()
        elif user_status == 'new user':
            new_user()
    except:
        return "Invalid"




(welcome())