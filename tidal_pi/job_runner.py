import time
from threading import Thread


class JobRunner():

    def __init__(self, job, sleep_seconds):
        self.job = job
        self.sleep_seconds = sleep_seconds
        self.stopped = True

    def start(self):
        self.stopped = False
        self.job_thread = Thread(target=self.run)
        return self.job_thread

    def run(self):
        while(self.stopped == False):
            self.job.run()
            time.sleep(self.sleep_seconds)

    def stop(self):
        self.run = False
