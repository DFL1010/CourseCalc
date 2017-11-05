from Mark import Mark
from Leg import Leg
from Course import Course

a = Mark("A", "Northern", 50, -4.5)
b = Mark("B", "Bay", 50, -5)
c = Mark("C", "Central", 50.5, -5.0)
d = Mark("D", "Central1", 50, -4.0)
e = Mark("E", "Testmark2", 49, -4.0)

marklist = []
leglist = []


def inputter():
    print("Enter your first mark (A, B, C, D, E)")
    instr = input()
    if instr.upper()[0] == "A":
        marklist.append(a)
    elif instr.upper()[0] == "B":
        marklist.append(b)
    elif instr.upper()[0] == "C":
        marklist.append(c)
    elif instr.upper()[0] == "D":
        marklist.append(d)
    elif instr.upper()[0] == "E":
        marklist.append(e)


"""
done = False

while not done:
    inputter()
    print("Done? ")
    fin = input()
    if fin.upper() == "Y":
       done = True
       """
print("\n")
leglist = [Leg(a, b, 0), Leg(b, c, 0)]
ab = Course(1, 4, leglist, 270)
print(ab.length())

ab.legs(leglist)
