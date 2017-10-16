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
    if instr == "A":
        marklist.append(a)
    elif instr == "B":
        marklist.append(b)
    elif instr == "C":
        marklist.append(c)
    elif instr == "D":
        marklist.append(d)
    elif instr == "E":
        marklist.append(e)

done = False

while not done:
    inputter()
    print("Done? ")
    fin = input()
    if fin == "Y":
       done = True 
       
print("\n\n")

for mark in marklist:
    try:
        print(mark.name)
    except AttributeError:
        print("ERROR: {}".format(mark))
