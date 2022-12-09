import curses
from curses import wrapper
import time


def starting_message(terminalScr):
    terminalScr.clear()
    terminalScr.addstr("Welcome to the Typing Speed Game!")
    terminalScr.addstr("\nPress the ANY key to continue!")
    terminalScr.refresh()
    terminalScr.getkey()
    # todo add a way to read the inputed key. like enter / escape / etc.
    # terminalScr.clear()
    # terminalScr.addstr("That wasn't the ANY key, that was just {inputed_key}")
    # terminalScr.addstr("You know what, it's fine. Let's just get this started.")


def display_text(terminalScr, sample, current, wpm):
    terminalScr.addstr(sample)
    terminalScr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = sample[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        terminalScr.addstr(0, i, char, color)


def wpm_calc(terminalScr):
    sample_text = "Hello friend! Glad to see you have made it this far. Take a seat and hear my tale."
    current_text = []
    wpm = 0
    # todo see if you can switch from the time thing to a spotwatch of sorts
    start_time = time.time()
    terminalScr.nodelay(True)
    while True:
        # exp am facut cu max si 1 ca sa evitam posibilitatea de 0 division
        time_elapsed = max(time.time() - start_time, 1)
        # todo in loc sa consideri average word len si sa calculezi asa, ia tasta "space" in considerare si calculeaza dupa asta.
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        terminalScr.clear()
        display_text(terminalScr, sample_text, current_text, wpm)
        terminalScr.refresh()

        if "".join(current_text) == sample_text:
            terminalScr.nodelay(False)

        try:
            key = terminalScr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if ord(key) == 8:
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(sample_text):
            current_text.append(key)


def main(terminalScr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    starting_message(terminalScr)
    wpm_calc(terminalScr)


wrapper(main)
