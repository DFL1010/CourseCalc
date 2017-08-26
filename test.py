from Mark import Mark
from Leg import Leg

a = Mark("A", "Northern", 50.5, -5)
b = Mark("B", "Bay", 50, -5.50)

ab = Leg(a, b)
print(ab.tCourse())
