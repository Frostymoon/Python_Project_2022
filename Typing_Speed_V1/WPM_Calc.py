from Stopwatch import *
from Viewer import *

def wpm_calc(terminal_scr, test_view: Viewer):
    sample_text = test_view.sample_text
    current_text = []
    wpm = 0
    # todo see if you can switch from the time thing to a spotwatch of sorts
    terminal_scr.nodelay(True)

    watchstopped = Stopwatch()

    while True:

        wpm = watchstopped.time_calc(current_text)

        terminal_scr.clear()
        test_view.display_wpm(terminal_scr, sample_text, current_text, wpm)
        terminal_scr.refresh()

        if "".join(current_text) == sample_text:
            terminal_scr.nodelay(False)

        try:
            key = terminal_scr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if ord(key) == 8:
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(sample_text):
            current_text.append(key)