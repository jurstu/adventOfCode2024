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


def checkMe(x, y):
    if(getC(x, y) == "A"):
        if((getC(x+1, y+1) == "S" and getC(x-1, y-1) == "M") or (getC(x+1, y+1) == "M" and getC(x-1, y-1) == "S")):
            if((getC(x-1, y+1) == "S" and getC(x+1, y-1) == "M") or (getC(x-1, y+1) == "M" and getC(x+1, y-1) == "S")):
                return 1
    return 0
    
output = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        output += checkMe(x, y)
        
print(output)
    




