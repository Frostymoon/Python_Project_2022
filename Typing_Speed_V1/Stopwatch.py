import time

class Stopwatch:
    start_time = 0.0

    def __init__(self):
        self.start_time = time.time()

    def GetTimeElapsed(self):
        time_elapsed = max(time.time() - self.start_time, 1)
        return time_elapsed

    def time_calc(self, current_text):
        time_elapsed = self.GetTimeElapsed()
        # todo in loc sa consideri average word len si sa calculezi asa, ia tasta "space" in considerare si calculeaza dupa asta.
        final_time = round((len(current_text) / (time_elapsed / 60)) / 5)
        return final_time