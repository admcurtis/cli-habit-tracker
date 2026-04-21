#%%
import json
from datetime import datetime



class HabitTracker():

    def __init__(self, data):
        self.data = data

    def habit_create(self, habit_name):
        if habit_name in self.data["habits"]:
            print(f"'{habit_name}' already exists!")
            return
        self.data["habits"][habit_name] = {
            "id": len(self.data["habits"]) + 1,
            "created": datetime.today().strftime("%Y-%m-%d")
        }
    
    def track_session(self, habit, session_length):
        if habit not in self.data["habits"]:
            print(f"{habit} does not exist")
            return
        try:
            session_length = int(session_length)
        except ValueError:
            print("Please provide the session length as minutes using an integer")
            return
        session = {}
        session["id"] = self.data["habits"][habit]["id"]
        session["date"] = datetime.today().strftime("%Y-%m-%d")
        session["duration"] = session_length
        self.data["sessions"].append(session)

