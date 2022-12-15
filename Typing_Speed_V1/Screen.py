import curses
from msvcrt import getch
from Data import *

class Screen:
    sample_text = ''
    difficulty = ""
    terminal_scr = ''
    data: Data

    def __init__(self, terminal_scr, data: Data):
        self.data = data
        self.terminal_scr = terminal_scr
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

# todo clean code and put difficulty_check method in its own module
# todo put all textx in a separate json and put in in a separate class
    def difficulty_check(self):
        self.terminal_scr.clear()
        self.terminal_scr.addstr("""How good are you?\n
        1. Not that great.
        2. Eh...decent.
        3. Pretty good.
        4. Keyboard GOD!\n""")
        self.difficulty = self.terminal_scr.getkey()
        self.data.set_gameplay_text(self.difficulty)
        self.terminal_scr.clear()
        
        match self.difficulty:
            case "1":
                self.terminal_scr.addstr(
                    "1. Well at least you're aware of your skills. Here we go!")
            case "2":
                self.terminal_scr.addstr(
                    "2.Most people lie int this bracket and you're no different. Not standing out at all...")
            case "3":
                self.terminal_scr.addstr(
                    "3. Well look who's confident in themselves! Ok, hotshot. Let's see what you've got.")
            case "4":
                self.terminal_scr.addstr(
                    "4. Quidquid Latine dictum sit, altum videtur\nAMEN")
            case _:
                self.terminal_scr.addstr(
                    "?. Started strong right out the gates, huh... How 'bout you give it another go.")
                self.difficulty_check()
                return None               
        self.terminal_scr.getch()
        return self.difficulty

    def starting_message(self):
        self.terminal_scr.clear()
        self.terminal_scr.addstr("Welcome to the Typing Speed Game!")
        self.terminal_scr.addstr(
            "\nFeel at ease using our 'Applicant Skill Screener', used by Bing.")
        self.terminal_scr.refresh()
        self.terminal_scr.getkey()

    def end_screen(self)->bool:

        self.terminal_scr.addstr(2, 0, "Nicely done! Would you like to go again?")
        self.terminal_scr.addstr(3, 0, "y/n")
        key_press = self.terminal_scr.getkey()
        match key_press.lower():
            case "y":
                # self.terminal_scr.
                self.terminal_scr.clear()
                return True
                # check if
            case "n":
                self.terminal_scr.clear()
                self.terminal_scr.addstr("Well OK then. Enter your name: \n ")
                user_name = self.terminal_scr.getkey()
                return False
            case _:
                self.terminal_scr.addstr(
                    "Bruh... Testing is over you can relax.\n PLAY AGAIN?!")
                self.terminal_scr.refresh()
                self.terminal_scr.clear()
                self.end_screen()
                return None
    # def data_storage():

    def display_wpm(self, terminal_scr, sample, current, wpm):
        terminal_scr.addstr(sample)
        terminal_scr.addstr(1, 0, f"WPM: {wpm}")

        for i, char in enumerate(current):
            correct_char = sample[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            terminal_scr.addstr(0, i, char, color)
