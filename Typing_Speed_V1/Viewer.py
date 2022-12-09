from argparse import Namespace
import curses
import random

class Viewer:
    sample_text = ''

    def __init__(self):
        self.sample_text = self.TextSampler()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def TextSampler(self):
        with open('samples.txt', 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip()

    def display_wpm(self, terminal_scr, sample, current, wpm):
        terminal_scr.addstr(sample)
        terminal_scr.addstr(1, 0, f"WPM: {wpm}")

        for i, char in enumerate(current):
            correct_char = sample[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)

            terminal_scr.addstr(0, i, char, color)

    def starting_message(self, terminal_scr):
        terminal_scr.clear()
        terminal_scr.addstr("Welcome to the Typing Speed Game!")
        terminal_scr.addstr("\nPress the ANY key to continue!")
        terminal_scr.refresh()
        terminal_scr.getkey()
        # todo add a way to read the inputed key. like enter / escape / etc.
        # terminal_scr.clear()
        # terminal_scr.addstr("That wasn't the ANY key, that was just {inputed_key}")
        # terminal_scr.addstr("You know what, it's fine. Let's just get this started.")