class Course:
    """
    This class takes as arguments the group and course, reads the coursecard
    and creates instances of Leg for each leg of the course.
    """
    def __init__(self, group, course, leglist):
        self.group = group
        self.course = course
        self.leglist = leglist

    def legs(self):
        # Take a list of legs, iterate of over it and output tCourse and distance
        for leg in self.leglist:
            print(leg.tCourse())
            print(leg.distance())

    def _readMarks():
        pass

    def isValid():
        pass

    def length():
        pass
