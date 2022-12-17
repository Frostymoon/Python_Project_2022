from Stopwatch import *
from Screen import *


class Wpm:
    loadedData: Data
    sample_text = ""
    current_text = []
    wpm = 0
    deleted_char = []

    def __init__(self, data: Data):
        self.loadedData = data

    def wpm_calc(self, terminal_scr, test_view: Screen) -> bool:
        self.init_data()
        # todo see if you can switch from the time thing to a stopwatch of sorts
        terminal_scr.nodelay(True)
        watchstopped = Stopwatch()

        while True:

            wpm = watchstopped.time_calc(self.current_text)
            
            terminal_scr.clear()
            test_view.display_wpm(terminal_scr, self.sample_text, self.current_text, wpm)
            terminal_scr.refresh()
            
            try:
                key = terminal_scr.getkey()
            except:
                continue
            
            # todo fix keys err in terminal
            if ord(key) == 27:  # escape key
                break

            if ord(key) == 8:   # backspace key
                if len(self.current_text) > 0:
                    self.deleted_char.append(self.current_text.pop())
            elif len(self.current_text) < len(self.sample_text):
                self.current_text.append(key)
                
            if "".join(self.current_text) == self.sample_text:

                SaveManager.set_current_wpm(wpm)
                SaveManager.set_deleted_characters(self.deleted_char)
                return True
    
    def init_data(self):
        self.current_text = []
        self.wpm = 0
        self.wpm_list = []
        self.sample_text = self.loadedData.get_currently_selected_text()
