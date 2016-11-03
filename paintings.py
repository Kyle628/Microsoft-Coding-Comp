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
"""for color in line:
    if color == prevColor and color in primaryColors:
        sys.stdout.write("blank ")
    elif color in primaryColors:
        sys.stdout.write(color + " ")
    elif color == prevColor and color not in primaryColors:
        pass
    else:
        if color != "blank\n":
            sys.stdout.write(comboColors[color] + " ")
    prevColor = color;"""

count = 0
for color in line:
    if color not in primaryColors:
        if color == "purple":
            if prevColor == "blue":
                if count == len(line) - 1:
                    sys.stdout.write("red")
                else:
                    sys.stdout.write("red ")
                    prevColor = "red"
            elif prevColor == "red":
                if count == len(line) - 1:
                    sys.stdout.write("blue")
                else:
                    sys.stdout.write("blue ")
                    prevColor = "blue"
            else:
                if count == len(line) - 1:
                    sys.stdout.write(comboColors[color])
                else:
                    sys.stdout.write(comboColors[color] + " ")
                    prevColor = color
        elif color == "orange":
            if prevColor == "red":
                if count == len(line) - 1:
                    sys.stdout.write("yellow")
                else:
                    sys.stdout.write("yellow ")
                    prevColor = "yellow"
            elif prevColor == "yellow":
                if count == len(line) - 1:
                    sys.stdout.write("red")
                else:
                    sys.stdout.write("red ")
                    prevColor = "red"
            else:
                if count == len(line) - 1:
                    sys.stdout.write(comboColors[color])
                else:
                    sys.stdout.write(comboColors[color] + " ")
                    prevColor = color
        elif color == "green":
            if prevColor == "blue":
                if count == len(line) - 1:
                    sys.stdout.write("yellow")
                else:
                    sys.stdout.write("yellow ")
                    prevColor = "yellow"
            elif prevColor == "yellow":
                if count == len(line) - 1:
                    sys.stdout.write("blue")
                else:
                    sys.stdout.write("blue ")
                    prevColor = "blue"
            else:
                if count == len(line) - 1:
                    sys.stdout.write(comboColors[color])
                else:
                    sys.stdout.write(comboColors[color] + " ")
                    prevColor = color
    elif color == prevColor and color in primaryColors:
        if count == len(line) - 1:
            sys.stdout.write("blank")
        else:
            sys.stdout.write("blank ")
            prevColor = "blank"
    elif color in primaryColors:
        if count == len(line) - 1:
            sys.stdout.write(color)
        else:
            sys.stdout.write(color + " ")
            prevColor = color
    else:
        if color != "blank\n":
            pass
    count += 1
