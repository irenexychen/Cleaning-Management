__author__ = 'Xiang-Yi'


class CleaningProgress:  #Observer's subject
    def __init__(self):
        self.observer = None

    def attach(self, outerObserver):
        self.observer = outerObserver

    def notify(self,robotIdentity):
        self.observer.update(robotIdentity)

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, cleaningProgress):
        self._progress = cleaningProgress
        if cleaningProgress == True:
            self.notify()

