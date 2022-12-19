import json
import pathlib
import random
ROOT = pathlib.Path(__file__).parent


class Data:
    """
    Scoate random text din json in functie de inputul playerului
    """
    the_json = {}
    __currently_selected_text = ''

    def __init__(self):
        self.load_json()

    def load_json(self):
        with open(ROOT / 'samples.json', 'r') as file:
            self.the_json = json.load(file)

    def get_difficulty_data(self, key: str):
        return self.the_json[key]

    def get_random_text(self, key: str):
        value = random.choice(list(self.get_difficulty_data(key)))
        return self.the_json[key][value]

    def set_gameplay_text(self, key: str):
        self.__currently_selected_text = self.get_random_text(key)

    def get_currently_selected_text(self):
        return self.__currently_selected_text