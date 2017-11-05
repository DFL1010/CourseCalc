class Course:

    def __init__(self, group, course, leglist, winddir):
        self.group = group
        self.course = course
        self.leglist = leglist
        self.winddir = winddir

    def _readCourseCard(self):
        with open("CourseCard.csv") as c:
            coursecard = c.read()

    def _readMarks():
        with open("Buoys10.csv") as f:
            marklist = f.read()

    def legs(self, leglist):
        # Take a list of legs, iterate of over it and output methods
        for leg in self.leglist:
            print(leg.tack)
            print(leg.angle)

        def isValid(self):
            pass

    def length(self):
        totallength = 0
        for leg in self.leglist:
            totallength += leg.distance()
        return totallength
#       print("Course Length: {}".format(totallength))


####
# What needs to be  returned?
# TWA for each leg
# Leg length
#
