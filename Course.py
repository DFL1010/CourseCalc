class Course:
    """
    This class takes as arguments the group and course, reads the coursecard
    and creates instances of Leg for each leg of the course.
    """
    def __init__(self, group, course, leglist, winddir):
        self.group = group
        self.course = course
        self.leglist = leglist
        self.winddir = winddir

    def legs(self):
        # Take a list of legs, iterate of over it and output methods
        for leg in self.leglist:
            print("True course: {}".format(leg.tCourse()))
            print("Leg Distance: {}".format(leg.distance()))
            print("TWA: {}".format(leg._twa()))

    def _readMarks():
        with file.open("Buoys10.csv") as f:
            f.read()
 

    def isValid():
        pass

    def length(self):
       totallength = 0
       for leg in self.leglist:
           totallength += leg.distance()
       #  return length
       print("Course Length: {}".format(totallength))

