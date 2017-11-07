from Mark import Mark
from Leg import Leg
from Course import Course


marklist = []
leglist = []

a = Mark('A','Northern',50.135,-5.042)
b = Mark('B','Bay' ,50.108,-5.0)
c = Mark('C','Central',50.12,-5.033)
cn = Mark('Cn','SKB Sails',50.145,-5.02)

"""
def inputter():
    print("Enter your first mark (A, B, C, D, E)")
    instr = input()
    if instr.upper()[0] == "A":
        marklist.append(a)
    elif instr.upper()[0] == "B":
        marklist.append(b)
    elif instr.upper()[0] == "C":
        marklist.append(c)

dcab = Course(1, 4, [d, c, a, b], 180)
print(dcab.leglist)
    elif instr.upper()[0] == "D":
        marklist.append(d)
    elif instr.upper()[0] == "E":
        marklist.append(e)
"""

"""
done = False

while not done:
    inputter()
    print("Done? ")
    fin = input()
    if fin.upper() == "Y":
       done = True
       """
ab = Course(1, 3, [Leg(a, c, 180), Leg(b, cn, 180)], 180)
print(ab.leglist)