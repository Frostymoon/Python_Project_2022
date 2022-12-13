from curses import wrapper
from Screen import *
from Stopwatch import *
from WPM_Calc import *
from Data import *


def main(terminal_scr):
    loadedData = Data()
    Screen_insance = Screen(terminal_scr, loadedData)
    wpm = Wpm(loadedData)
    Screen_insance.starting_message()
    Screen_insance.difficulty_check()
    wpm.wpm_calc(terminal_scr, Screen_insance)


wrapper(main)
