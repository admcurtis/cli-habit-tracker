import json

class JSONStorage():

    def __init__(self):
        ...

    def load(self): 
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {
                "habits": {},
                "sessions": {},
                "progress": {}
            }
        return data

    def save(self):
        ...