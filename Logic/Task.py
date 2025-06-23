from Repository.Task_Repository import *
import Models.Task as T


def add_task(conn,t_name,t_desc):
    task_repo = Task_Repository(conn)
    task1=task_repo.get_task_by_taskname(t_name.lower())

    if task1 is None:
        task_id= task_repo.create_task(T.Task(t_name.lower(),t_desc))
        if task_id is not None:
            return f"{t_name} added!"
        else:
            return "Action failed, Try again!"
    elif task1 is not None:
        if task1.task_name == t_name.lower():
            return f"{t_name} Already exists for use.."
        return None
    return None


def task_profile_update(conn,t_name,new_t_name,t_desc):
    task_repo = Task_Repository(conn)
    task1 = task_repo.get_task_by_taskname(t_name.lower())

    task1.task_name = new_t_name #Assigned new t_name
    task1.task_desc = t_desc

    task_repo.update_task(task1,task1.task_id)


def delete_task(conn,t_name):
    task_repo = Task_Repository(conn)
    task1 = task_repo.get_task_by_taskname(t_name.lower())

    if task1 is not None:
        task_repo.delete_task(task1.task_id)
        return f"{task1.task_name} deleted!"
    else:
         return "Task not found, Try again!"

def display_all_tasks(conn):
    task_repo = Task_Repository(conn)
    task1 = task_repo.get_all_tasks()




