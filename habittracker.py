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

