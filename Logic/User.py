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

