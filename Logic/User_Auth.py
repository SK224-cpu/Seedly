from Repository.User_Repository import *

def login(user_name,password,conn):
    user_repo = User_Repository(conn)
    user1=user_repo.get_user_by_username(user_name)
    if user1 != None:
        if (user1.password == password):
            return True
    else:
        return False
    