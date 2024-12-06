with open("input", "r") as f:
    d = f.read()


def isSubHere(s, sub, index=0):
    for i in range(len(sub)):
        if(s[i+index] != sub[i]):
            return 0
    return 1 

def isThisADigit(d):
    return ord('0') <= ord(d) and ord(d) <= ord('9')

# states:
# 0 - searching for "mul("
# 1 - found mul, checking number1
# 
state = 0


i = 0
start = 0
stop = 0
output = 0
while(i < d.__len__()):
    
    if(state == 0):
        #print(d[i:])
        if(isSubHere(d[i:], "mul(")):
            start = i
            state = 1
            #print("start is", d[i:i+4])
            i += 4
            
        else:
            i += 1

    if(state == 1):
        if(isThisADigit(d[i])):
            state = 1
            i+=1
        elif(d[i]==","):
            state = 2
            i+=1
        else:
            state = 0
            start = 0

    if(state == 2):
        if(isThisADigit(d[i])):
            state = 2
            i+=1
        elif(d[i]==")"):
            state = 3
            stop = i
            i+=1
        else:
            state = 0
            start = 0

    if(state == 3):
        ss = d[start:stop+1]
        nums = ss[4:-1].split(",")
        output += int(nums[0]) * int(nums[1])
        state = 0




print(output)
