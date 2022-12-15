import json
from json import JSONEncoder
import pathlib
ROOT = pathlib.Path(__file__).parent


class SaveManager:

    user_data = {}
    
    def __init__(self):
        pass

    def save_data(self, user_name: str, last_wpm: int, current_score: int, highscore: int, selected_difficulty: str):
        self.user_name = user_name
        self.last_wpm = last_wpm
        self.current_score = current_score
        self.highscore = highscore
        self.selected_difficulty = selected_difficulty
        self.save_to_json()

    def save_deleted_chars(self, x):
        self.deleted_chars.append(x)

    def create_user_json(self, some_json):
        some_json = json.dumps(self.user_data, indent=4, cls=PlayerEncoder)
        with open("user_data.json", "w") as file:
            file.write(some_json)

    def save_to_json(self):
        self.user_data["User Name"] = self.user_name
        self.user_data["Words/Minute"] = self.last_wpm
        self.user_data["Highscore"] = self.highscore
        self.user_data["Difficulty"] = self.selected_difficulty
        self.user_data["Deleted Characters"] = self.deleted_chars

        self.create_user_json(self.user_data)

class Player:
    user_name = ""
    rounds = []
    
    def __init__(self, user_name: str, rounds: list):
        self.user_name = user_name
        self.rounds = rounds
    
class Round:
    round_number = 0
    last_wpm = int()
    score = int()
    selected_difficulty = ""
    deleted_chars = []
    
    def __init__(self, round_number, last_wpm, score, selected_difficulty, deleted_chars):
        self.round_number = round_number
        self.last_wpm = last_wpm
        self.score = score
        self.selected_difficulty = selected_difficulty
        self.deleted_chars = deleted_chars
        
class PlayerEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__