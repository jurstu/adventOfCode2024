
with open("input", "r") as f:
    d = f.read()

l = d.split("\n")
l = [[int(x) for x in y.split(" ")] for y in l]
print(l)

def checkLine(line):
    lastSign = (line[0] - line[1]) > 0
    for i in range(len(line) - 1):
        
        this = line[i]
        nexxt = line[i+1]
        diff = abs(this - nexxt)
        sign = (this - nexxt) > 0
        if(sign == lastSign and diff >= 1 and diff <= 3):
            pass
        else:
            return 0
    return 1

output = 0
for line in l:
    if(checkLine(line)):
        output+= 1

print(output)




