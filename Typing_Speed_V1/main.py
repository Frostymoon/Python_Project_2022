from curses import wrapper
from Screen import *
from Stopwatch import *
from WPM_Calc import *

def main(terminal_scr):
    Screen_insance = Screen()
    Screen_insance.starting_message(terminal_scr)
    wpm_calc(terminal_scr, Screen_insance)

wrapper(main)