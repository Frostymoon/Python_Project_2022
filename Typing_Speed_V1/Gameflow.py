from Screen import *
import SaveManager
from SaveManager import *
from WPM_Calc import Wpm


class Gameflow:
    diff = ''
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
        self.diff = self.Screen_insance.difficulty_check()
        if self.diff != None:
            self.Gameplay()
            
    def Gameplay(self):
        isGameFinished = self.wpm.wpm_calc(self.terminal_scr, self.Screen_insance)
        if isGameFinished:
            self.End()

    def End(self):
        should_continue = self.Screen_insance.end_screen()
        SaveManager.set_current_difficulty(self.diff)
        if should_continue:
            SaveManager.save_user_data()
            # save data
            self.Start()
        else:
            SaveManager.save_user_data()
            # call create PDF, and in that thing open the right json with the user_name from the SaveManager
            exit()
            # quit and save data