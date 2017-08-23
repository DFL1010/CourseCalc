class Leg:
    def __init__(self, markA, markB):
        self.markA = markA
        self.markB = markB

    def mLat(self):
        return round(((abs(self.markB.lat - self.markA.lat)) / 2), 4) * 60

    def dLong(self):
        return round(abs(self.markB.ltude - self.markA.ltude), 4) * 60

    def length(self):
        pass
