import time
from threading import Thread
import logging
import sys


class JobRunner():

    def __init__(self, name, job, sleep_seconds):
        self.name = name
        self.job = job
        self.sleep_seconds = sleep_seconds
        self.stopped = True

    def start(self):
        self.stopped = False
        self.job_thread = Thread(target=self.run)
        self.job_thread.start()
        return self.job_thread

    def run(self):
        while(self.stopped == False):
            logging.info("running {}".format(self.name))
            try:
                self.job.run()
            except:
                logging.error("error running job {}".format(self.name), sys.exc_info()[0])

            logging.info("finished running {}".format(self.name))
            logging.info("{} sleeping for {}".format(self.name, self.sleep_seconds))
            time.sleep(self.sleep_seconds)
            logging.info("{} awake".format(self.name))

    def stop(self):
        self.run = False
