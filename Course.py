from Leg import Leg
from Mark import Mark


class Course:

    def __init__(self, group, course, leglist, winddir):
        self.group = group
        self.course = course
        self.leglist = leglist
        self.winddir = winddir
        self.llegs = list()
        self.legs()

    def _readCourseCard(self):
        with open("CourseCard.csv") as c:
            coursecard = c.read()

    def _readMarks():
        with open("Buoys10.csv") as f:
            marklist = f.read()

    def legs(self):
        # Take a list of legs, iterate of over it and output methods
        for i in range(len(self.leglist)):
            self.llegs.append(Leg(self.leglist[i], self.leglist[i+1], self.winddir))

    def isValid(self):
        pass

    def length(self):
        totallength = 0
        for leg in self.llegs:
            totallength += leg.distance()
        return totallength
#       print("Course Length: {}".format(totallength))


####
# What needs to be  returned?
# TWA for each leg
# Leg length
#
