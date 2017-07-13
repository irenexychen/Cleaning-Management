__author__ = 'Xiang-Yi'

class Cleaniness():
    _roomCleaniness = []                #Singleton
    _width = 0
    _length = 0

    def __init__(self):
        if len(self._roomCleaniness) == 0:
            self.readFile()

    def printList(self):
        for i in range(len(self._roomCleaniness)):
            for k in range(len(self._roomCleaniness[i])):
                print(i, k, ":", self._roomCleaniness[i][k])

    def readFile(self):
        with open("house_data.txt") as f:
            self._width, self._length = f.readline().split(' ')
            for line in f:
                self._roomCleaniness.append(line.strip().split(" "))

        self.TotalHouse = len(self._roomCleaniness)

    @property
    def roomcleaniness(self):
        return self._roomCleaniness

    @property
    def width(self):
        return int(len(self._roomCleaniness))

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def length(self):
        return int(len(self._roomCleaniness[0]))

    @length.setter
    def length(self, value):
        self._length = value

    def __str__(self):
        return str(self._roomCleaniness)



