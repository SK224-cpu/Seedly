import psycopg2

class Task():
    def __init__(self,task_name,task_desc=str(),task_id=None):
        self.task_id = task_id
        self.task_name = task_name 
        self.task_desc = task_desc

    def __repr__(self):
        return f"Task(task_id={self.task_id!r}, task_name={self.task_name!r}, task_desc={self.task_desc!r})"


