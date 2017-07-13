__author__ = 'Xiang-Yi'

from SweepingRobot import SweepingRobot
from MoppingRobot import MoppingRobot
from RobotFactory import RobotFactory
from RobotObserver import RobotObserver
from CleaningProgress import CleaningProgress

from Cleaniness import Cleaniness



class Management():


    def __init__(self):
        self.houseone = Cleaniness()
        self.mopper = None
        self.sweeper = None
        self.cleaningObserver = RobotObserver()
        self.cleaningSubject = CleaningProgress()
        self.cleaningSubject.attach(self.cleaningObserver)

    def doManagement(self):
        if self.checkToMop() == True:
            self.mopper = RobotFactory(MoppingRobot())
            self.mopper.getRobot().startToMop(self.cleaningSubject)
        if self.checkToSweep() == True:
            self.sweeper = RobotFactory(SweepingRobot())
            self.sweeper.getRobot().startToSweep(self.cleaningSubject)

    def checkToMop(self):
        mop = 0
        for i in range(len(self.houseone.roomcleaniness)):
            for k in range(len(self.houseone.roomcleaniness[i])):
                if self.houseone.roomcleaniness[i][k] == "M":
                    mop = mop + 1
        if mop >= (self.houseone.TotalHouse *0.1):                             #assumes mopping must be done when over 30% dirty
            return True

    def checkToSweep(self):
        sweep = 0
        for i in range(len(self.houseone.roomcleaniness)):
            for k in range(len(self.houseone.roomcleaniness[i])):
                if self.houseone.roomcleaniness[i][k] == "S":
                    sweep = sweep + 1
        if sweep >= (self.houseone.TotalHouse *0.1):                             #assumes sweeping must be done when over 30% dirty
            return True




