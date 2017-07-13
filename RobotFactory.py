__author__ = 'Xiang-Yi'


class RobotFactory:                             #AbstractFactory
    def __init__(self, concreteRobot):
        self._robot = concreteRobot

    def getRobot(self):
        return self._robot