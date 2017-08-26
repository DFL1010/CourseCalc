import math


class Leg:
    def __init__(self, markA, markB):
        self.markA = markA
        self.markB = markB

    def _mLat(self):
        return ((abs(self.markB.lat - self.markA.lat)) / 2) * 60

    def _dLat(self):
        return (abs(self.markB.lat - self.markA.lat)) * 60

    def _dLong(self):
        return abs(self.markB.longt - self.markA.longt)

    def _dep(self):
        return (self._dLong() * math.cos(self._mLat())) * 60

    def distance(self):
        return round(math.sqrt((self._dep() ** 2) + (self._dLat() ** 2)), 4)

    def tCourse(self):
        # Tan = (dep / dLat)
        # Quadrantal notation
        pass
