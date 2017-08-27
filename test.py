from Mark import Mark
from Leg import Leg

a = Mark("A", "Northern", 50, -4.5)
b = Mark("B", "Bay", 50, -5)

ab = Leg(a, b)
print(ab.tCourse())
