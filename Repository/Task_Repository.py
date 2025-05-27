import Models.Task as T

class Task_Repository:
    def __init__(self, conn):
        self.conn = conn

    def create_task(self, task: T.Task):
        with self.conn.cursor() as task_cursor:
            task_cursor.execute ("""INSERT INTO tasks_details (task_name,task_desc) 
                                VALUES (%s,%s) RETURNING task_id""", 
                                (task.task_name, task.task_desc) )
            new_task=task_cursor.fetchone()[0]
        return(new_task)
    
    def get_all_tasks(self):
        with self.conn.cursor() as task_cursor:
            task_cursor.execute("SELECT * FROM tasks_details")
            print_tasks=task_cursor.fetchall()
            tasks = []
            for row in print_tasks:
                tasks.append(T.Task(row[1],row[2], row[0]))
            return tasks
    
    def update_task(self, task:T.Task, task_id:int):
        with self.conn.cursor() as cur:
            cur.execute("""Update tasks_details set task_name=%s, task_desc=%s where task_id=%s """, ( T.task_name, T.task_desc, task_id))
        self.conn.commit()

    def delete_user(self,task_id):
        with self.conn.cursor() as cur:
            cur.execute("""delete from tasks_details where task_id=%s""", (task_id,))
        self.conn.commit()
    
    def get_user_by_TaskId(self, task_id):
        with self.conn.cursor() as cur:
            cur.execute("select * from tasks_details where task_id =%s", (task_id,))
            row = cur.fetchone()
            if row:
                task_id, task_name, task_desc= row
                return T.Task(task_id, task_name, task_desc = id)
        return None