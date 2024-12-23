import numpy as np

with open("input", "r") as f:
    d = f.read()

d = d.strip()
connections = d.split("\n")
nameDir = {}
for con in connections:
    c1, c2 = con.split("-")    
    nameDir[c1] = 1
    nameDir[c2] = 1

#print(nameDir) 

names = list(nameDir.keys())

for i, name in enumerate(names):
    nameDir[name] = i    

rel = np.zeros([len(names), len(names)])


for con in connections:
    c1, c2 = con.split("-")
    i1, i2 = nameDir[c1], nameDir[c2]
    
    rel[i1, i2] = 1
    rel[i2, i1] = 1

print(names)
print(len(names))
print(rel)    




threes = {}

def sortThree(a, b, c):
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    return a, b, c


for row in range(rel.shape[0]):
    for col in range(rel.shape[1]):
        if(rel[row,col] == 0):
            pass
        else:
            # we got 1, so we have to attack the next row
            for i, (a, b) in enumerate(zip(rel[row], rel[col])):
                if(a==1 and b==1 and (i!=row) and (i!=col)):
                    # winner winner, chicken dinner
                    a, b, c = sortThree(row, col, i)
                    threes[a, b, c] = 1

for k in threes.keys():
    print(k)

#print(len(threes.keys()))
 

output = 0

for k in threes.keys():
    a, b, c = k
    a, b, c = names[a], names[b], names[c]
    print(a, b, c)
    if("t" in a) or ("t" in b) or ("t" in c):
        output += 1

print(output)

#print(threes)


 
       



