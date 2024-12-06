
import numpy as np

f = open("input", "r")
d = f.read()
f.close()


lines = d.split("\n")
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



print(blockers, guard)

output = 0
currentDir = [0, -1]
while(True):
    guardDesc = f"{guard[0]}:{guard[1]}"
    if(not guardDesc in visited):
        output+=1
        visited[guardDesc] = 1
    
    
    
    nextPos = np.array(currentDir) + np.array(guard)
    print(nextPos)
    nextDesc = f"{nextPos[0]}:{nextPos[1]}"
    
    if(not nextDesc in m):
        # out of bounds
        #print(m)
        #print(nextDesc)
        print(output)
        exit()
    
    
        



    if(m[nextDesc] == "#"):
        currentDir = nextDir[str(currentDir)]
    else:
        guard = nextPos.tolist()



    #print(i)


