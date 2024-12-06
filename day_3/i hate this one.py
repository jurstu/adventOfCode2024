with open("input", "r") as f:
    d = f.read()


import time

ind = 0
output = 0

candidates = []
while(ind < len(d)):
    try:
        ii = d[ind:].index("mul(") + ind
        ind = ii+1
        print("ind is", ind)
    except:
        ind+=1
        continue
    
    candidates.append(ii)
    #time.sleep(2)



print(candidates)

for i in range(len(candidates)):

    start = candidates[i]
    if i == len(candidates) - 1:
        end = len(d)
    else:
        end = candidates[i+1]

    subs = d[start:end]
    try:
        endd = subs.index(")")
    except:
        continue

    subs = subs[:endd]
    
    ss = subs[4:].split(",")
    print(ss)
    
    
