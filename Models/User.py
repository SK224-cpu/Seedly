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

    def __repr__(self):
        return (f"User(user_id={self.user_id!r}, user_name={self.user_name!r}, "
                f"first_name={self.first_name!r}, last_name={self.last_name!r}, "
                f"dob={self.dob!r}, objective={self.objective!r}, "
                f"creation_date={self.creation_date!r}, lock_account={self.lock_account!r}, "
                f"last_login={self.last_login!r})")
    