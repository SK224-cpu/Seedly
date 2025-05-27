
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

    

# de = DailyEntry(
#     user_id=1,
#     task_id=101,
#     task_done=True,
#     timestamp="2023-10-01T12:00:00Z",
#     note="Completed the task successfully.",
#     daily_entry_id=1
# )
# de = DailyEntry(8,2,True,datetime.datetime.now(), "Bahoot cycling kar rahye ho aaj kal")
# # print(de)

#print(de.create_daily_entry(conn))
# allactivities = de.get_all_daily_entries(conn)
# print(len(allactivities))
# check_last_activity_done(allactivities)
# dailyEntry = de.get_daily_entry_by_id(conn,4)
# dailyEntry = de.get_daily_entry_by_user_id(conn,7)
# print(len(dailyEntry))
# dailyEntry = de.get_daily_entry_by_task_id(conn,1)
# print(len(dailyEntry))
# de.task_status=False
# de.timestamp=datetime.datetime.now()
# de.update_daily_Entries(conn,1)

# new_daily_entry_id = de.create_daily_entry(conn)
# print(new_daily_entry_id)

# de.delete_daily_entry(conn,6)