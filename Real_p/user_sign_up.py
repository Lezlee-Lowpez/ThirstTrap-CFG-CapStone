import re


class MaxCharacterCount(Exception):
    pass


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def check(new_user_email):
    if re.fullmatch(regex, new_user_email):
        return new_user_email
    else:
        print("Invalid Email")


regularExpression = "^[A-Za-z][A-Za-z0-9_]{7,19}$"


def check_username(username):
    regex = "^[A-Za-z]\\w{4,14}$"
    r = re.compile(regex)

    if (re.search(r, username)):
        return username
    else:
        print("Not Valid")
