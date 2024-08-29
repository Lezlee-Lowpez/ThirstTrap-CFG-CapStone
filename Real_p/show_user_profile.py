from user_login_signup_handling import CheckExistenceOfPlants

# this only works for users that only have one plant registered, figure out how to query more!

# sup = CheckExistenceOfPlants('valpal')
# print(sup.execute_query())


def profile(current_user_name):
    hi = CheckExistenceOfPlants(current_user_name)
    user_account = (list(hi.execute_query()))
    print(f"""
Hello {current_user_name},
  Here is you current plant profile!
  ----------------------------------------
  Your {user_account[0]}, {user_account[1]}, was last watered on {user_account[2]} 
  and needs to be watered every {user_account[3]} day/s.
  ----------------------------------------
""")
