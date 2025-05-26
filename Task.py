import psycopg2

class Task():
    def __init__(self,task_name,task_desc=str(),task_id=None):
        self.task_id = task_id
        self.task_name = task_name 
        self.task_desc = task_desc

    def create_task(self,conn):
        with conn.cursor() as task_cursor:
            task_cursor.execute ("Insert into tasks_details (task_name,task_desc)values (%s,%s) returning task_id", (self.task_name, self.task_desc) )

            new_task=task_cursor.fetchone()[0]
        return(new_task)
    
    def get_all_tasks(self,conn):

        with conn.cursor() as task_cursor:
            task_cursor.execute("select * from tasks_details")

            print_tasks=task_cursor.fetchall()
            tasks = []
            for row in print_tasks:
                # taskid, taskname, taskdesc = row
                tasks.append(Task(row[1],row[2], row[0]))
            return tasks

            # for task in print_tasks:
            #     #print(type(task))
            #     task_id, task_name, task_desc = task
            #     print(f"ID: {task_id}, Name: {task_name}")

    # def get_all_tasks_by_id(task_id,conn):
    #     with conn.cursor() as task_cursor:
    #         task_cursor.execute(f"select task_id, task_name from tasks_details where task_id= {task_id}")
