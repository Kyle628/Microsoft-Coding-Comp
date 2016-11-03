import sys


lines = []


def findMissingNums(line):
    minimum = min(line)
    maximum = max(line)
    allNums = []
    missingNums = []
    for i in range(minimum, maximum):
        allNums.append(i)

    for num in allNums:
        if num not in line:
            missingNums.append(num)

    return missingNums

with open('./practiceinput2.txt') as f:
    for line in f: # read rest of lines
        lines.append([int(x) for x in line.split()])
    f.close()

lines.pop(0)

for line in lines:
    missingNums = findMissingNums(line)
    for num in missingNums:
        if(not missingNums):
            break
        sys.stdout.write(str(num) + " ")
    if not missingNums:
        print "\n"
