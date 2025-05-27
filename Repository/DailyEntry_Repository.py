import Models.DailyEntry as DE

class DailyEntry_Repository:
    def __init__(self, conn):
        self.conn = conn

    def create_daily_entry(self, de:DE.DailyEntry):
        with self.conn.cursor() as curr:
            curr.execute("""INSERT INTO daily_entry (user_id, task_id, task_status, timestamp, note) 
                            VALUES (%s, %s, %s, %s, %s) 
                            RETURNING daily_entry_id""", 
                            (de.user_id, de.task_id, de.task_status, de.timestamp, de.note))
            dailyEntryId = curr.fetchone()[0]
            self.conn.commit()
        return dailyEntryId
    
    def get_all_daily_entries(self):
        with self.conn.cursor() as curr:
            curr.execute("SELECT * FROM daily_entry")
            dailyentries=curr.fetchall()
            list_of_daily_entries=[]
            for row in dailyentries:
                obj=DE.DailyEntry(daily_entry_id=row[0],user_id=row[1],task_id=row[2],task_status=row[3],timestamp=row[4],note=row[5])
                list_of_daily_entries.append(obj)
            return list_of_daily_entries
    
    def get_daily_entry_by_user_id(self, userId:int):
        with self.conn.cursor() as curr:
            curr.execute(f"SELECT * FROM daily_entry WHERE user_id ={userId}")
            dailyentries=curr.fetchall()
            list_of_daily_entries=[]
            for row in dailyentries:
                obj=DE.DailyEntry(daily_entry_id=row[0],user_id=row[1],task_id=row[2],task_status=row[3],timestamp=row[4],note=row[5])
                list_of_daily_entries.append(obj)
            return list_of_daily_entries 
    
    def get_daily_entry_by_task_id(self, taskId:int):
        with self.conn.cursor() as curr:
            curr.execute(f"SELECT * FROM daily_entry WHERE task_id = {taskId}")
            dailyentries=curr.fetchall()
            list_of_daily_entries=[]
            for row in dailyentries:
                obj=DE.DailyEntry(daily_entry_id=row[0],user_id=row[1],task_id=row[2],task_status=row[3],timestamp=row[4],note=row[5])
                list_of_daily_entries.append(obj)
            return list_of_daily_entries

    def get_daily_entry_by_id(self, daily_entry_id:int):
        with self.conn.cursor() as curr:
            curr.execute(f"SELECT * FROM daily_entry WHERE daily_entry_id ={daily_entry_id}")
            dailyentry=curr.fetchone()
            return DE.DailyEntry(daily_entry_id=dailyentry[0], user_id=dailyentry[1],task_id=dailyentry[2],task_status=dailyentry[3],timestamp=dailyentry[4],note=dailyentry[5])  

    def update_daily_Entries(self, de:DE.DailyEntry, daily_entry_id:int):
        with self.conn.cursor() as cur:
            cur.execute("""UPDATE daily_entry SET task_status=%s,timestamp=%s WHERE daily_entry_id= %s""", (de.task_status, de.timestamp, daily_entry_id))
        self.conn.commit()

    def delete_daily_entry(self, daily_entry_id:int):
        with self.conn.cursor() as curr:
            curr.execute(f"DELETE FROM daily_entry WHERE daily_entry_id={daily_entry_id}")
        self.conn.commit()