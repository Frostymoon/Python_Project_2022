import curses
import random
import json
import Scoring
import pathlib
ROOT = pathlib.Path(__file__).parent


class Screen:
    sample_text = ''

    def __init__(self):
        self.sample_text = self.TextSampler()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def difficulty_check(self, difficulty):
        match difficulty:
            case "1":
                print("Well at least you're aware of your skills. Here we go!")
            case "2":
                print("Most people lie int this bracket and you're no different. Not standing out at all...")
            case "3":
                print("Well look who's confident in themselves! Ok, hotshot. Let's see what you've got.")
            case "4":
                print("Quidquid Latine dictum sit, altum videtur\nAMEN")
            case _ :
                print("Started strong right out the gates, huh... How 'bout you givbe it another go.")
                Screen.difficulty_check()
                
    def starting_message(self, terminal_scr):
        terminal_scr.clear()
        terminal_scr.addstr("Welcome to the Typing Speed Game!")
        terminal_scr.addstr(("""\nFeel at ease using our "Applicant Skill Screener", used by Bing. 
                1. Not that great.
                2. Eh...decent.
                3. Pretty good.
                4. Keyboard GOD!"""))

        terminal_scr.getkey()
        terminal_scr.clear()
        # Scoring.difficulty_check()
        # terminal_scr.refresh()
        # terminal_scr.getkey()
#         terminal_scr.clear()
#         terminal_scr.addstr("""That wasn't the ANY key...")
# You know what, it's fine. Let's just get this started.""")
    
# todo figure out how to pass Scoring.difficulty instead of 1 in chosen_difficulty
    def TextSampler(self):
        with open(ROOT / 'samples.json', 'r') as file:
            lines = json.load(file)
            chosen_difficulty = random.choice(list(lines["1"]))
        return(lines["1"][chosen_difficulty])

    def display_wpm(self, terminal_scr, sample, current, wpm):
        terminal_scr.addstr(sample)
        terminal_scr.addstr(1, 0, f"WPM: {wpm}")

        for i, char in enumerate(current):
            correct_char = sample[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            terminal_scr.addstr(0, i, char, color)
