with open ("input", "r") as f:
    d = f.read()
    d.strip()
    d = d.split("\n")[0]

# 12345
# %2 = 1
# last block is 5, so ind=-1

backIndex = -1
checksum = 0
checksumInd = 0
if((len(d)-1)%2 == 0):
    # we got 1 block, 1 space arrangement
    backIndex = -1
else:
    backIndex = -2
    # we got 1 block left
print("last block is", d[backIndex])

i = 0

while(i < len(d)):
    if(i%2 == 0):
        checksum+=int(d[i]) * checksumInd
        print("added ", d[i], "to the checksum", checksum)
        checksumInd+=1
    else:
        ll = int(d[i])
        print("adding ", ll, "back entries")
        for l in range(ll):
            #             ////////////
            checksum+=int(d[backIndex]) * checksumInd
            print("added ", d[backIndex], "to the checksum =", checksum)
            checksumInd+=1
            backIndex-=2
    
    #if(len(d) + backIndex <= i):
    #    break

    i+=1 


print(checksum)
# 12345
# 1..3....5
# 153......
# 0, 5, 11

#2333133121414131402
#00...111...2...333.44.5555.6666.777.888899
#0099811188827773336446555566
