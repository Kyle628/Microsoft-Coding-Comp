import sys
lines = []

with open('./painting.txt') as f:
    for line in f: # read rest of lines
        line.split(' ')
        lines.append(line)
    f.close()

line = lines[0].split(" ")

comboColors = {"purple": "red blue", "green": "blue yellow", "orange": "red yellow"}
primaryColors = ['red', 'yellow', 'blue']

prevColor = "start"

count = 0
for color in line:
    if color not in primaryColors:
        if color == "purple":
            if prevColor == "blue":
                sys.stdout.write("red ")
                prevColor = "red"
            elif prevColor == "red":
                sys.stdout.write("blue ")
                prevColor = "blue"
            else:
                sys.stdout.write(comboColors[color] + " ")
                prevColor = color
        elif color == "orange":
            if prevColor == "red":
                sys.stdout.write("yellow ")
                prevColor = "yellow"
            elif prevColor == "yellow":
                sys.stdout.write("red ")
                prevColor = "red"
            else:
                sys.stdout.write(comboColors[color] + " ")
                prevColor = color
        elif color == "green":
            if prevColor == "blue":
                sys.stdout.write("yellow ")
                prevColor = "yellow"
            elif prevColor == "yellow":
                sys.stdout.write("blue ")
                prevColor = "blue"
            else:
                sys.stdout.write(comboColors[color] + " ")
                prevColor = color
    elif color == prevColor and color in primaryColors:
        sys.stdout.write("blank ")
        prevColor = "blank"
    elif color in primaryColors:
        sys.stdout.write(color + " ")
        prevColor = color
    else:
        pass
    count += 1
