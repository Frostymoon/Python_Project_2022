import curses
from curses import wrapper
from Screen import *
from Stopwatch import *
from WPM_Calc import *

def main(terminal_scr):
    Screen_insance = Screen(terminal_scr)
    Screen_insance.starting_message()
    Screen_insance.difficulty_check()
    wpm_calc(terminal_scr, Screen_insance)

wrapper(main)