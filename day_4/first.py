import numpy as np

with open("input", "r") as f:
    d = f.read()

WORD = "XMAS"
lines = d.split("\n")

def getC(x, y):
    if(x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)):
        return lines[y][x]
    else:
        return "."


def checkMe(x, y, di):
    l = len(WORD)
    pos = [x, y]
    for i in range(l):
        print("pos is", pos)
        if(getC(*pos) == WORD[i]):
            # we good, move the pawn
            pos = np.array(np.array(pos) + np.array(di)).tolist()
        else:
            return 0
    return 1
    
output = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        output += checkMe(x, y, [0, 1])
        output += checkMe(x, y, [0, -1])
        output += checkMe(x, y, [1, 0])
        output += checkMe(x, y, [-1, 0])

        output += checkMe(x, y, [1, 1])
        output += checkMe(x, y, [1, -1])

        output += checkMe(x, y, [-1, 1])
        output += checkMe(x, y, [-1, -1])

print(output)
    




