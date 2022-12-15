from Screen import *
from WPM_Calc import Wpm


class Gameflow:
    Screen_insance: Screen
    wpm: Wpm
    terminal_scr = ""

    def __init__(self, Screen_insance: Screen, wpm: Wpm, terminal_scr):
        self.Screen_insance = Screen_insance
        self.terminal_scr = terminal_scr
        self.wpm = wpm

    def Start(self):
        self.Screen_insance.starting_message()
        diff = self.Screen_insance.difficulty_check()
        if diff != None:
            self.Gameplay()
        # difficulty check returneaza finalul deciziei jucatorului si updateaza data
        # depizand de rezultatul de la diffuculty, intra in GAmeplay phase

    def Gameplay(self) -> bool:  # TEMP PARAM
        # vrem sa returneze daca e gata runda
        isGameFinished = self.wpm.wpm_calc(self.terminal_scr, self.Screen_insance)
        # call to end
        if isGameFinished:
            self.End()

    def End(self):
        self.terminal_scr.nodelay(False)
        should_continue = self.Screen_insance.end_screen()
        if should_continue:
            # find way to restart
            # save data
            self.wpm.initData()
            self.Start()
        else:
            print("p")
            # quit and save data
