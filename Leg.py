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
        return abs((self._dLong() * math.cos(self._mLat()))) * 60

    def distance(self):
        return math.sqrt((self._dep() ** 2) + (self._dLat() ** 2))

    def tCourse(self):
        # Quadrantal notation
        isN = False
        isE = False
        try:
            intAngle = math.degrees(math.atan(self._dep() / self._dLat()))
        except ZeroDivisionError:
            intAngle = 90
            
        if self._dLat() > 0:
            # b is north of a
            isN = True
        elif self._dLat() < 0:
            # b is south of a
            isN = False
        else:
            # E/w.Note self._dLat() == 0, so intAngle gives div0 error
            intAngle = 90

        if self._dLong() > 0:
            # b is east of a
            isE = True
        elif self._dLong() < 0:
            # b is west of a
            isE = False
        else:
            # N/S
            return "else"

        # Calc Quadrantal notation from isN, isE
        if isN and isE:
            return intAngle
        elif isN and not isE:
            return 360 - intAngle
        elif not isN and isE:
            return 180 - intAngle
        else:
            return 180 + intAngle
