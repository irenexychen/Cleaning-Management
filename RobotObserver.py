__author__ = 'Xiang-Yi'
from Cleaniness import Cleaniness

class RobotObserver:
    def __init__(self):
        self.houseone = Cleaniness()

    def update(self, robotIdentity):                                                                      #can later change room after updated
        print("Robot Observer has determined that %s Robot has finished cleaning the room" % robotIdentity)
        self.houseone.printList()

