
class DailyEntry:
    def __init__(self, user_id, task_id, task_status, timestamp, note, daily_entry_id=None):
        self.user_id = user_id
        self.task_id = task_id
        self.task_status = task_status
        self.timestamp = timestamp
        self.note = note
        self.daily_entry_id = daily_entry_id
    
    def __repr__(self):
        return f"DailyEntry(user_id={self.user_id}, task_id={self.task_id}, task_done={self.task_status}, timestamp={self.timestamp}, note={self.note}, daily_entry_id={self.daily_entry_id})"