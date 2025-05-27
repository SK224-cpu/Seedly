import Models.User as U

class User_Repository:
    def __init__(self, conn):
        self.conn = conn

    def create_user(self, u:U.User):
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO user_details (
            password, first_name, last_name, dob,
            objective, creation_date, lock_account, last_login,user_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning user_id""", (u.password, u.first_name, u.last_name, u.dob, u.objective, u.creation_date, u.lock_account, u.last_login, u.user_name))

            new_user = cur.fetchone()[0]
        self.conn.commit()
        return (new_user)
    
    def update_user(self, u:U.User, user_id):
        with self.conn.cursor() as cur:
            cur.execute("""Update user_details set  password = %s, first_name = %s, last_name = %s, dob = %s,
            objective = %s, creation_date = %s, lock_account = %s, last_login = %s,user_name = %s where user_id = %s """, (u.password, u.first_name, u.last_name, u.dob, u.objective, u.creation_date, u.lock_account, u.last_login, u.user_name,user_id))
        self.conn.commit()
    
    def getAll_users(self):
            with self.conn.cursor() as cur:
                cur.execute("select * from user_details;")
                get_all_rows = cur.fetchall()
                users = []
                for row in get_all_rows:
                            id, password, first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name = row
                            users.append(U.User(password,first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name, user_id = id))
                
                return users
    
    def get_user_by_UserId(self, user_id:int):
        with self.conn.cursor() as cur:
            cur.execute(f"select * from user_details where user_id = {user_id}")
            row = cur.fetchone()
            if row:
                id, password, first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name = row
                return U.User(password,first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name, user_id = id)
        return None
    
    def delete_user(self,user_id):
        with self.conn.cursor() as cur:
            cur.execute("""delete from user_details where user_id = %s""", (user_id,))
        self.conn.commit()

    def get_user_by_username(self,user_name_exists):
        with self.conn.cursor() as cur:
            cur.execute("select * from user_details where user_name = %s", (user_name_exists,))
            row = cur.fetchone()
            if row:
                id, password, first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name = row
                return U.User(password,first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name, user_id = id)
        return None

