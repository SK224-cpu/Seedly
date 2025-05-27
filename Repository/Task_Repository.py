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
        return new_task
    
    def get_all_tasks(self):
        with self.conn.cursor() as task_cursor:
            task_cursor.execute("SELECT * FROM tasks_details")
            print_tasks=task_cursor.fetchall()
            tasks = []
            for row in print_tasks:
                tasks.append(T.Task(row[1],row[2], row[0]))
            return tasks
        
    # def get_all_tasks_by_id(task_id,conn):
    #     with conn.cursor() as task_cursor:
    #         task_cursor.execute(f"select task_id, task_name from tasks_details where task_id= {task_id}")