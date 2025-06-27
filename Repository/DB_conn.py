from configparser import ConfigParser
from psycopg2.pool import SimpleConnectionPool


class DBconn:
    def __init__(self, config_path="config/config.ini"):
        config = ConfigParser()
        config.read(config_path)

        self.host_var = config['DB']['host']
        self.database_var = config['DB']['database']
        self.user_var = config['DB']['user']
        self.password_var = config['DB']['password']
        #conn = psycopg2.connect(host=host_var, database=database_var, user=user_var, password=password_var)
        self.pool = SimpleConnectionPool(minconn = 1, maxconn = 10, host=self.host_var, database=self.database_var,
                                         user=self.user_var, password=self.password_var)

    def get_conn(self):
        return self.pool.getconn()

    def return_conn(self, conn):
        return self.pool.putconn(conn)

    def close_conn(self):
        return self.pool.closeall()
        