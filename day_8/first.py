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
            print(diffX, diffY, "###", posBarr)

            finalPos1 = [
                posBarr[0] + diffX,
                posBarr[1] + diffY
            ]

            finalPos2 = [
                posAarr[0] - diffX,
                posAarr[1] - diffY
            ]

            

            print("final positions", finalPos1, finalPos2)
            f1 = f"{finalPos1[1]}:{finalPos1[0]}"
            f2 = f"{finalPos2[1]}:{finalPos2[0]}"
            
            if(isInMap(finalPos1)):
                allAntinodes[f1] = 1
            if(isInMap(finalPos2)):
                allAntinodes[f2] = 1

print(len(allAntinodes.keys()))



