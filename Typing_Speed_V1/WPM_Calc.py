from Stopwatch import *
from Screen import *


class Wpm:
    loadedData: Data
    sample_text = ""
    current_text = []
    wpm = 0

    def __init__(self, data: Data):
        self.loadedData = data

    def wpm_calc(self, terminal_scr, test_view: Screen):
        self.initData()
        # todo see if you can switch from the time thing to a spotwatch of sorts
        terminal_scr.nodelay(True)
        watchstopped = Stopwatch()

        while True:

            wpm = watchstopped.time_calc(self.current_text)

            terminal_scr.clear()
            test_view.display_wpm(terminal_scr, self.sample_text, self.current_text, wpm)
            terminal_scr.refresh()

            if "".join(self.current_text) == self.sample_text:
                terminal_scr.nodelay(False)
                test_view.end_screen()
                self.initData()

            try:
                key = terminal_scr.getkey()
            except:
                continue
            
            # todo fix keys err in terminal
            if ord(key) == 27:  # escape key
                break

            if ord(key) == 8:   # backspace key
                if len(self.current_text) > 0:
                    self.current_text.pop()
            elif len(self.current_text) < len(self.sample_text):
                self.current_text.append(key)

    def initData(self):
        self.current_text = []
        self.wpm = 0
        self.sample_text = self.loadedData.get_currently_selected_text()
