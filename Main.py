import datetime
from calendar import month
from configparser import ConfigParser
import psycopg2
from Repository.Task_Repository import *
from Repository.User_Repository import *
from Repository.DailyEntry_Repository import *
import Models.User as U
from Logic.User import *
from Logic.Task import *
import Models.DailyEntry as DE

def main():
        
        config=ConfigParser()
        config.read("config/config.ini")
        host_var=config['DB']['host']
        database_var=config['DB']['database']
        user_var=config['DB']['user']
        password_var=config['DB']['password']
        conn = psycopg2.connect(host=host_var,database=database_var,user=user_var,password=password_var) 

        # user1=u.User('***','Sweety','RRR',datetime.strptime('08/05/2000', '%d/%m/%Y'),'HAbit Tracker',datetime.now().strftime("%Y-%m-%d"),  False,datetime.now().strftime("%Y-%m-%d"),'sk@gmail.com')
        # Task_name = input("Enter a rabbit to track:  ")
        # task1=t.Task(Task_name,"None")
        #task1.create_task(conn)
        # print(type(conn))
        
        # print(task1.get_all_tasks(conn))
        #task1.get_all_tasks_by_id(1)

        # get_user_details=user1.getAll_users(conn)

        # for i in get_user_details:
        #         print(f"Id:{i.user_id} - Name: {i.first_name} {i.last_name}")


        # get_user_detail=user1.get_user_by_UserId(conn,23)
        # # if get_user_detail:
        # #         print(f"Id:{get_user_detail.user_id} - Name: {get_user_detail.first_name} {get_user_detail.last_name}")
        # # else:
        # #         print("User not found")

        # #print(type(user1))
        # # user1.password='##'
        # # user1.update(conn,23)
        # user1.delete_user(conn,21)

        #User_Repository1 = User_Repository(conn)
        
        # user1 = User_Repository1.get_user_by_UserId(26)
        # if user1!=None:
        #         user1.first_name = "Hulk"
        #         User_Repository1.update_user(user1,23)

        # for i in User_Repository1.getAll_users():
        #         print(f"Full Nme: {i.first_name} {i.last_name} Id: {i.user_id}")

 #        Name= user_signup('Aditya','I',datetime.date(2010, 5, 24)
 # ,'Habit tracker',"ai@gmail.com",'SD5648FF',conn)
 #        print(Name)

 #        user_profile_update('Aaaaaditya','I',datetime.date(2010, 5, 24)
 # ,'Habit tracker',"ai@gmail.com",'SD5648FF',conn)
 #
       # task = add_task(conn,"Hiking","Task")
       #  task = delete_task(conn, "Hiking")
       #  task = task_profile_update (conn,"Run","Run_123","Updated")

        # de = DE.DailyEntry(
        #             user_id=8,
        #             task_id=2,
        #             task_status = False,
        #             timestamp="2026-06-07T12:00:00Z",
        #             note="Completed the task successfully.",
        #             task_completed = False)
        # task = DailyEntry_Repository(conn)
        # task1 = task.task_streak_monthwise(7,6,2025)
        # # task1 = task.create_daily_entry(de)
        # print(task1)

        login_result = user_login("sk@gmail.com_9","***", conn)
        print(login_result)
if __name__== "__main__":
        main()


