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

print(string)

def findLastDigit(text: str):
    for i, c in enumerate(reversed(text)):
        #print(len(text) - i - 1, c)
        if(type(c) == int):
            return len(text) - i - 1, c


#findLastDigit("asdf1234")

string = list(string)
out = ""
i = 0
while(i < len(string)):
    c = string[i]
    if(c == "."):
        ind, char = findLastDigit(string)
        if(ind > i):
            string[i] = char
            string[ind] = "."
        else:
            break
    else:
        pass
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