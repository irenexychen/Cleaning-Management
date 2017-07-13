__author__ = 'Xiang-Yi'
from Cleaniness import Cleaniness

class MoppingRobot:
    def __init__(self):
        self.houseone = Cleaniness()

    def doJob(self, i, k):
        self.houseone.roomcleaniness[i][k] = "0"                      #location (i, k) became clean

    def startToMop(self, cleaningProgress):
        for i in range(len(self.houseone.roomcleaniness)):
            for k in range(len(self.houseone.roomcleaniness[i])):
                if self.houseone.roomcleaniness[i][k] == "M":
                    self.doJob(i, k)
                if self.checkComplete(i, k) == True:
                    cleaningProgress.notify(self.robotName)                           #room completely mopped, observer is notified

    def checkComplete(self, i, k):
        if ((i == (len(self.houseone.roomcleaniness) - 1)) and (k == (len(self.houseone.roomcleaniness[i]) - 1))):
            return True
        return False

    def __str__(self):
        return "Mopping Robot called."

    @property
    def robotName(self):
        return "Mopping"