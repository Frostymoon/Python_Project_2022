from curses import wrapper
from Viewer import *
from Stopwatch import *
from WPM_Calc import *

def main(terminal_scr):
    viewer_insance = Viewer()
    viewer_insance.starting_message(terminal_scr)
    wpm_calc(terminal_scr, viewer_insance)

wrapper(main)