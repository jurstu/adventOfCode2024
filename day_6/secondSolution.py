
import numpy as np
from numba import jit

f = open("input", "r")
d = f.read()
f.close()


lines = d.split("\n")

def solve(lines, blocker) -> int:
    blockers = {}
    m = {}
    visited = {}

    nextDir = {
        "[0, -1]": [1, 0],
        "[1, 0]": [0, 1],
        "[0, 1]": [-1, 0],
        "[-1, 0]": [0, -1],

    }

    guard = [0,0]
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            desc = f"{x}:{y}"
            if(c == "#"):
                blockers[desc] = 1
            if(c == "^"):
                guard = [x, y]
            m[desc] = c



    #print(blockers, guard)
    blockers[blocker] = 1
    m[blocker] = "#"


    currentDir = [0, -1]
    dirNum = 0 # 0, 1, 2, 3
    while(True):
        #print(guard)
        guardDesc = f"{guard[0]}:{guard[1]}:{dirNum}"
        if(not guardDesc in visited):
            visited[guardDesc] = 1
        else:
            return 1
        
        
        
        nextPos = np.array(currentDir) + np.array(guard)
        #print(nextPos)
        nextDesc = f"{nextPos[0]}:{nextPos[1]}"
        
        if(not nextDesc in m):
            # out of bounds
            return 0 # out of bounds

        if(m[nextDesc] == "#"):
            currentDir = nextDir[str(currentDir)]
            dirNum = (dirNum+1)%4
        else:
            guard = nextPos.tolist()



    #print(i)

def solveeee():
    output = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            #print(lines[y])
            if(lines[y][x] == "."):
                output += solve(lines, f"{x}:{y}")
                #print(f"{x}:{y}")
        print(f"{y/len(lines) * 100}")
    print(output)


solveeee()