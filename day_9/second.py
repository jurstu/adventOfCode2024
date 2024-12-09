with open ("input", "r") as f:
    d = f.read()


isBlock = 1
string = []
idd = 0
for c in d:
    if(isBlock):
        l = int(c)
        string += [idd] * l
        idd+=1
    else:
        l = int(c)
        string += "." * l

    isBlock = 1 - isBlock

def findLastDigit(text: str):
    for i, c in enumerate(reversed(text)):
        #print(len(text) - i - 1, c)
        if(type(c) == int):
            return len(text) - i - 1, c



def findSpace(text):
    spaceOn = 0
    l = 0
    start = 0
    for i, c in enumerate(text):
        if(spaceOn == 0):
            if(type(c) == str):
                spaceOn = 1
                l = 1
                start = i
            else:
                pass
        else:
            if(type(c) == str):
                l+=1
            else:
                break
    return start, l



def getLastBlock(text):
    isBlock = 0
    for i, c in enumerate(reversed(text)):
        if(isBlock == 0):
            if(type(c) != str):
                isBlock = 1
                l = 1
                start = i
            else:
                pass
        else:
            if(type(c) != str):
                l+=1
            else:
                break
    return len(text) - start - 1, l




#findLastDigit("asdf1234")

string = list(string)
backString = string.copy()



out = ""
i = 0
while(i < len(string)):
    c = string[i]
    if(type(c) == str):
        start, l = findSpace(string[i:])
        start2, l2 = getLastBlock(backString)
        backString = backString[]
        if(l >= l2):
            # check this
            string[start:start+l2] = backString[start2:start2+l2]
        else:
            while(l < l2):
                
            
        



    print(i/len(string))
    i+=1
#0099811188827773336446555566
#0099811188827773336446555566..............
#print("".join(string))

checksum = 0
for i, c in enumerate(string):
    if(c != "."):
        checksum += i * int(c)
    else:
        break

print(checksum)

# tried
#90008815667