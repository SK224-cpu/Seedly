import datetime
import Models.DailyEntry as D
from Repository.User_Repository import *
from Repository.DailyEntry_Repository import *

def user_login(user_name,password,conn):
    user_repo = User_Repository(conn)
    user1=user_repo.get_user_by_username(user_name)
    if user1 is not None:
        if user1[2] == password:
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
            return "This password is too easy to guess. Please create a new one.",0
        elif len(password) >12:
            return "This password is too long. Please create a new one.",0
        else:
            return "User created",user_repo.create_user(U.User(password,first_name, last_name, dob, objective, datetime.datetime.now(),False,
                                  datetime.datetime.now(), user_name ))
    else:
        return f"{user_name} Already exists", 0

def user_profile_update(first_name,
                last_name,
                dob,
                objective,
                user_id,conn):
    user_repo = User_Repository(conn)
    user_obj = user_repo.get_user_by_userid(user_id)
    if user_obj is not None:
        user_obj.first_name=first_name
        user_obj.last_name=last_name
        user_obj.dob=dob
        user_obj.objective=objective

        user_repo.update_user(user_obj,user_obj.user_id)
        return "Updated!"
    else:
        return "User doesn't exist!"

def user_password_update(password, user_id,conn):
    user_repo = User_Repository(conn)
    user_obj = user_repo.get_user_by_userid(user_id)
    if user_obj is not None:
        user_obj.password = password
        print(user_obj)
        user_repo.update_user(user_obj,user_obj.user_id)
        return "Password Updated!"
    else:
        return "User doesn't exist!"

def display_tasks_by_user(user_id,conn):
    task_repo= DailyEntry_Repository(conn)
    task1 = task_repo.get_tasks_of_user(user_id)

def display_count_of_task_id(user_id, month, year, conn):
    task_repo= DailyEntry_Repository(conn)
    task1 = task_repo.task_streak_monthwise(user_id, month, year)

def add_task_to_track(user_id, task_id,conn):
    task_repo = DailyEntry_Repository(conn)
    task1 = task_repo.get_tasks_of_user(user_id)
    if task1.count() < 5:
        task_DE = D.DailyEntry(user_id,task_id,False,datetime.datetime.now(),"", False)
        Daily_Entry_task_id = task_repo.create_daily_entry(task_DE)
        return task_id
    else:
        return "your 5 task limit reached"

def fetch_all_user(conn):
    user_repo = User_Repository(conn)
    user_var = user_repo.getAll_users()
    return user_var

def fetch_user_detail(user_id,conn):
    user_repo = User_Repository(conn)
    user_var = user_repo.get_user_by_UserId(user_id)
    return user_var

def delete_user (user_id,conn):
    user_repo = User_Repository(conn)
    user1 = user_repo.get_user_by_UserId(user_id)
    if user1 is not None:
        user_repo.delete_user(user_id)
        return f"{user1.user_name} Deleted!"
    else:
        return "User doesn't exists!"

