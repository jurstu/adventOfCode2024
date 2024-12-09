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
lastId = 0
if((len(d))%2 == 0):
    # we got 1 block, 1 space arrangement
    backIndex = -1
    IDS_TOTAL = (len(d))//2
    

    print("parity")
else:
    backIndex = -2
    IDS_TOTAL = (len(d)+1)//2
    # we got 1 block left
    print("non parity")

print("last block is", d[backIndex])
print(IDS_TOTAL)

backId = IDS_TOTAL -1
frontId = 0

i = 0

frontAssets = int(d[0])

backAssets = 0

print("iterating")
while(i < len(d)):
    if(i%2 == 0):
        ll = int(d[i])
        for l in range(ll):
            checksum+=frontId * checksumInd
            print("adding id", frontId)
            frontId+=1
            checksumInd+=1

    else:
        ll = int(d[i])
        
        for l in range(ll):
            #             ////////////
            checksum+=backId * checksumInd
            print("adding id", backId)
            #print("added ", int(backId), "to the checksum =", checksum)
            
            backId-=1
            checksumInd+=1
            backIndex-=2
            print(backIndex)
    
    if(len(d) + backIndex <= i):
        break

    i+=1 


print(checksum)
# 12345
# 1..3....5
# 153......
# 0, 5, 11

#2333133121414131402
#00...111...2...333.44.5555.6666.777.888899
#0099811188827773336446555566
