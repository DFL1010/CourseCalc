from Mark import Mark
from Leg import Leg

a = Mark("A", "Northern", 50, -4.5)
b = Mark("B", "Bay", 50, -5)

c = Mark("C", "Central", 50.5, -5.0)
d = Mark("D", "D", 50, -5.0)


ab = Leg(a, b)
print(ab.tCourse())

cd = Leg(c, d)
print(cd.tCourse())
