import json
from json import JSONEncoder
import pathlib
import os
from fpdf import FPDF
ROOT = pathlib.Path(__file__).parent

user_name = ''
current_round = 1
current_wpm = 0
current_score = 0
current_accuracy = 0
current_difficulty = ''
current_deleted_characters = []


def set_user_name(name: str):
    global user_name
    user_name = name


def set_current_round(round: int):
    global current_round
    current_round = round + 1


def set_current_wpm(wpm: int):
    global current_wpm
    current_wpm = wpm


def set_current_score(score: int):
    global current_score
    current_score = score

def set_current_accuracy(accuracy):
    global current_accuracy
    current_accuracy = accuracy
    
    

def set_current_difficulty(difficulty: str):
    global current_difficulty
    current_difficulty = difficulty


def set_deleted_characters(deleted_characters: list):
    global current_deleted_characters
    current_deleted_characters = deleted_characters


def save_user_data():
    round = Round(current_round, current_wpm, current_score, current_accuracy,
                  current_difficulty, current_deleted_characters)
    user = Player(user_name, [round])
    create_json(user)


def save_round_data():
    round = Round(current_round, current_wpm, current_score,current_accuracy,
                  current_difficulty, current_deleted_characters)
    return round


def save_deleted_chars(self, x):
    self.deleted_chars.append(x)


def create_json(user_data):
    json_path = os.path.exists(ROOT / f"{user_name}.json")
    if json_path:
        loaded_user = load_json()
        set_current_round(len(loaded_user.rounds))
        loaded_user.rounds.append(save_round_data())
        player_data = json.dumps(loaded_user, indent=4, cls=PlayerEncoder)
        with open(ROOT / f"{user_name}.json", "w") as file:
            file.write(player_data)
    else:
        player_data = json.dumps(user_data, indent=4, cls=PlayerEncoder)
        with open(ROOT / f"{user_name}.json", "w") as file:
            file.write(player_data)

    file.close()


def load_json():
    with open(ROOT / f"{user_name}.json", "r") as file:
        user = Player(**json.loads(file.read()))
        
        for index, item in enumerate(user.rounds):
            temp_json = json.dumps(item, indent=4)
            temp = Round(**json.loads(temp_json))
            user.rounds[index] = temp

        return user

def json_2_pdf():
    with open(ROOT / f'{user_name}.json', 'r') as f:
        data = json.load(f)

    name = data['user_name']
    dictionaries_list = data['rounds']

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.cell(0, 10, txt=name)

    pdf.ln()

    for d in dictionaries_list:
        for key, value in d.items():
            pdf.cell(0, 10, txt='{}: {}'.format(key, value))
            pdf.ln()

    pdf.output(f'{user_name}.pdf', 'F')

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
    accuracy = int()
    selected_difficulty = ""
    deleted_chars = []

    def __init__(self, round_number, last_wpm, score, accuracy, selected_difficulty, deleted_chars):
        self.round_number = round_number
        self.last_wpm = last_wpm
        self.score = score
        self.accuracy = accuracy
        self.selected_difficulty = selected_difficulty
        self.deleted_chars = deleted_chars


class PlayerEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
