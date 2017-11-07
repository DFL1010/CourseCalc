import csv

courselist = list()

with open("mylorcc.csv") as f:
    coursereader = csv.reader(f)
    for line in coursereader:
        courselist.append(line)

for line in courselist:
    string =