import datetime
import Models.User as U
from Repository.User_Repository import *

def login(user_name,password,conn):
    user_repo = User_Repository(conn)
    user1=user_repo.get_user_by_username(user_name)
    if user1 is not None:
        if user1.password == password:
            return True
        return False
    else:
        return False

def user_signup(first_name,
                last_name,
                dob,
                objective,
                user_name,password,conn): #to create new users login details

    user_repo = User_Repository(conn)

    #Check if already exists
    user1 = user_repo.get_user_by_username(user_name)
    if user1 is None:
        if len(password) < 6:
            return "This password is too easy to guess. Please create a new one."
        elif len(password) >12:
            return "This password is too long. Please create a new one."
        else:
            return user_repo.create_user(U.User(password,first_name, last_name, dob, objective, datetime.datetime.now(),False,
                                  datetime.datetime.now(), user_name ))
    else:
        return f"{user_name} Already exists"

def user_profile_update(first_name,
                last_name,
                dob,
                objective,
                user_name,password,conn):
    user_repo = User_Repository(conn)
    user_obj = user_repo.get_user_by_username(user_name)

    user_obj.first_name=first_name
    user_obj.last_name=last_name
    user_obj.dob=dob
    user_obj.objective=objective
    user_obj.password=password

    user_repo.update_user(user_obj,user_obj.user_id)



    