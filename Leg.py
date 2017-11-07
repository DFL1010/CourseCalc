from Mark import Mark
import math
import csv

class Leg:
    def __init__(self, markA, markB, winddir):
        self.markA = markA
        self.markB = markB
        self.winddir = winddir
        self.tco = self.tCourse()
        self.twa()
        self.buoylist = list()
        #self.readmarks(self)
        #self.buoyinst()

    @staticmethod
    def readmarks(self):
        with open("Buoys10.csv") as f:
            buoyreader = csv.reader(f, delimiter=',')
            for row in buoyreader:
                self.buoylist.append(row)

    def _mLat(self):
        return ((abs(self.markB.lat - self.markA.lat)) / 2) * 60

    def _dLat(self):
        return (abs(self.markB.lat - self.markA.lat)) * 60

    def _dLong(self):
        return abs(self.markB.longt - self.markA.longt)

    def _dep(self):
        return abs((self._dLong() * math.cos(self._mLat()))) * 60

    def _recurse(self, degs):
        if degs < 360:
            return degs
        else:
            degs -= 360
            return self._recurse(degs)

    def buoyinst(self):
        tempmA = list()
        tempmB = list()
        for row in self.buoylist:
            if row[0] == self.markA.code:
                tempmA.append(row)
            elif row[0] == self.markB.code:
                tempmB.append(row)
        self.markA = Mark(tempmA[0], tempmA[1], tempmA[2], tempmA[3])
        self.markB = Mark(tempmB[0], tempmB[1], tempmB[2], tempmB[3])

    def twa(self):
        # This should return R/G, 0-180
        if (self.tco > self.winddir) and (abs(self.tco - self.winddir) < 180):
            self.tack = "Port"
            self.angle = self.tCourse() - self.winddir
        elif self.tco < self.winddir and (abs(self.tco - self.winddir) < 180):
            self.tack = "Starboard"
            self.angle = self.winddir - self.tCourse()
        elif self.tco == self.winddir:
            self.tack = "Upwind"
            self.angle = 0
        else:
            self.tack = "Downwind"
            self.angle = 180
        # return "Boat is on {} tack with TWA of {}".format(tack, angle)

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
            intAngle = 0

        # Calc Quadrantal notation from isN, isE
        if isN and isE:
            return self._recurse(intAngle)
        elif isN and not isE:
            return self._recurse(360 - intAngle)
        elif not isN and isE:
            return self._recurse(180 - intAngle)
        else:
            return self._recurse(180 + intAngle)
