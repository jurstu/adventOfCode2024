with open ("input", "r") as f:
    d = f.read()

allAntinodes = {}

lines = d.split("\n")

antennas = {}

ww = len(lines[0])
hh = len(lines)

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        curPos = f"{y}:{x}"
        if(c != "."):
            if not c in antennas:
                antennas[c] = {}
            antennas[c][curPos] = [x, y]
            
print(antennas)


def isInMap(pos):
    if (pos[0] >= 0 and pos[0] < ww):
        if (pos[1] >= 0 and pos[1] < hh):
            return 1

    return 0


for antType, positions in antennas.items():
    print(antType, positions)
     
    for i, posA in enumerate(list(positions.keys())):
        for posB in list(positions.keys())[i+1:]:
            posAarr = positions[posA]
            posBarr = positions[posB]
            
            diffX = posBarr[0] - posAarr[0]
            diffY = posBarr[1] - posAarr[1]
            nextPoint = [
                            posBarr[0],
                            posBarr[1]
                        ]
            i = 1
            while(isInMap(nextPoint)):
                n = f"{nextPoint[1]}:{nextPoint[0]}"
                allAntinodes[n] = 1
                nextPoint = [
                            posBarr[0] - diffX * i,
                            posBarr[1] - diffY * i
                        ]
                i+=1
            nextPoint = [
                posBarr[0],
                posBarr[1]
            ]
            i = 1
            while(isInMap(nextPoint)):
                n = f"{nextPoint[1]}:{nextPoint[0]}"
                allAntinodes[n] = 1
                nextPoint = [
                            posBarr[0] + diffX * i,
                            posBarr[1] + diffY * i
                        ]
                i+=1


print(len(allAntinodes.keys()))



