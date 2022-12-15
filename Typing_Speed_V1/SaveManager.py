import json
from json import JSONEncoder
import pathlib
ROOT = pathlib.Path(__file__).parent


def save_user_data(user_name: str, current_round: int, current_wpm: int, current_score: int, current_difficulty: str, current_deleted_characters: list):
    round = Round(current_round, current_wpm, current_score,
                  current_difficulty, current_deleted_characters)
    user = Player(user_name, [round])
    create_json(user)


def save_deleted_chars(self, x):
    self.deleted_chars.append(x)


def create_json(user_data):
    player_data = json.dumps(user_data, indent=4, cls=PlayerEncoder)
    with open("user_data.json", "w") as file:
        file.write(player_data)


def load_json():
    with open(ROOT / "user_data.json", 'r') as file:
        user = Player(**json.loads(file.read()))
        
        for index, item in enumerate(user.rounds):
            temp_json = json.dumps(item, indent=4)
            temp = Round(**json.loads(temp_json))
            user.rounds[index] = temp
        return user


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
