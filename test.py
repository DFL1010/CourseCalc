from Mark import Mark
from Leg import Leg
from Course import Course

a = Mark("A", "Northern", 50.5, -5)
b = Mark("B", "Bay", 50, -5)

ab = Leg(a, b)

print(ab.distance())
