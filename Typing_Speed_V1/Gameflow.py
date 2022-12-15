from Screen import *
import SaveManager
from SaveManager import *
from WPM_Calc import Wpm


class Gameflow:
    Screen_insance: Screen
    wpm: Wpm
    terminal_scr = ""

    def __init__(self, Screen_insance: Screen, wpm: Wpm, terminal_scr):
        self.Screen_insance = Screen_insance
        self.terminal_scr = terminal_scr
        self.wpm = wpm
        self.Screen_insance.starting_message()
        self.Start()

    def Start(self):
        diff = self.Screen_insance.difficulty_check()
        if diff != None:
            self.Gameplay()
            
    def Gameplay(self):
        isGameFinished = self.wpm.wpm_calc(self.terminal_scr, self.Screen_insance)
        if isGameFinished:
            self.End()

    def End(self):
        self.terminal_scr.nodelay(False)
        should_continue = self.Screen_insance.end_screen()
        if should_continue:
            # save data
            self.Start()
        else:
            SaveManager.save_user_data()
            exit()
            # quit and save data