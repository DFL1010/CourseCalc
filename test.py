import math

from Mark import Mark
from Leg import Leg

a = Mark("A", "Northern", 50.5, -5)
b = Mark("B", "Bay", 50, -5.50)

ab = Leg(a, b)


ratio = ab._dep() / ab._dLat()
radians = math.atan(ratio)
degs = math.degrees(radians)

print(ratio)
print(radians)
print(degs)
print(ab.tCourse())
