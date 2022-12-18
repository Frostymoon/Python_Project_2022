from curses import wrapper
from Screen import *
from Stopwatch import *
from WPM_Calc import *
from Data import *
from Gameflow import *


def main(terminal_scr):
    loadedData = Data()
    Screen_insance = Screen(terminal_scr, loadedData)
    wpm = Wpm(loadedData)
    gameflow = Gameflow(Screen_insance, wpm, terminal_scr)

wrapper(main)