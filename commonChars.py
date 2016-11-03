import sys

lines = []

with open('./commonchars.txt') as f:
    for line in f: # read rest of lines
        lines.append(line.rstrip())
    f.close()

num_lines = int(lines.pop(0))

print num_lines
for line in lines:
    common_chars = []
    line_arr = line.split(' ')
    for char in line_arr[0]:
        common_chars.append(char)
    for word in line_arr:
        for char in common_chars:
            if char not in word:
                while char in common_chars:
                    common_chars.remove(char)
    common_chars = list(set(common_chars))
    common_chars.sort()
    for char in common_chars:
        sys.stdout.write(char)
    print ""
