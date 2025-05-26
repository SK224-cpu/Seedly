import psycopg2
class User:
    def __init__(self,password,
                first_name,
                last_name,
                dob,
                objective,
                creation_date,
                lock_account,
                last_login,
                user_name, user_id =None):
        self.user_id = user_id
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.objective=objective
        self.creation_date=creation_date
        self.lock_account=lock_account
        self.last_login=last_login
        self.user_name=user_name
 
    @staticmethod
    def maprowstoclass(rows):
        users = []
        for row in rows:
                     id, password, first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name = row
                     users.append(User(password,first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name, user_id = id))
        return users    

    def save_user(self,conn):
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO user_details (
            password, first_name, last_name, dob,
            objective, creation_date, lock_account, last_login,user_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) returning user_id""", (self.password,self.first_name,self.last_name,self.dob,self.objective,self.creation_date,self.lock_account,self.last_login,self.user_name))

            new_user = cur.fetchone()[0]
        conn.commit()
        return (new_user)
    
    def update_user(self,conn,user_id):
        with conn.cursor() as cur:
            cur.execute("""Update user_details set  password=%s, first_name=%s, last_name=%s, dob=%s,
            objective=%s, creation_date=%s, lock_account=%s, last_login=%s,user_name=%s where user_id=%s """, (self.password,self.first_name,self.last_name,self.dob,self.objective,self.creation_date,self.lock_account,self.last_login,self.user_name,user_id))
        conn.commit()
    
    def getAll_users(self,conn):
            with conn.cursor() as cur:
                cur.execute("select * from user_details;")  
                get_all_rows = cur.fetchall()
                users = User.maprowstoclass(get_all_rows)
            return users
    
    def get_user_by_UserId(self, conn, user_id):
        with conn.cursor() as cur:
              cur.execute("select * from user_details where user_id =%s", (user_id,))
              row = cur.fetchone()
              if row:
                    id, password, first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name = row
                    return User(password,first_name, last_name, dob, objective, creation_date, lock_account, last_login, user_name, user_id = id)
        return None
    
    def delete_user(self,conn,user_id):
        with conn.cursor() as cur:
            cur.execute("""delete from user_details where user_id=%s""", (user_id,))
        conn.commit()
