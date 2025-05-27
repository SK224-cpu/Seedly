from configparser import ConfigParser
import psycopg2
from Repository.Task_Repository import *
from Repository.User_Repository import *
from Repository.DailyEntry_Repository import *

def main():
        
        config=ConfigParser()
        config.read("config/config.ini")
        host_var=config['DB']['host']
        database_var=config['DB']['database']
        user_var=config['DB']['user']
        password_var=config['DB']['password']
        conn = psycopg2.connect(host=host_var,database=database_var,user=user_var,password=password_var) 

        user_repository1 = User_Repository(conn)
        print(user_repository1.getAll_users())

if __name__== "__main__":
        main()


