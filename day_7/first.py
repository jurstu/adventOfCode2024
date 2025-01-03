with open("input", "r") as f:
    d = f.read()





def solve(line):
    #print(line)
    res = int(line.split(":")[0])
    nums = line.split(":")[1]
    nums = [int(x) for x in nums.split(" ")[1:]]
    opNum = len(nums) - 1
    comb = 2**opNum
    print("for line", line, "I have", comb, "combinations")
    for i in range(comb):
        ops = [int(x) for x in bin(i)[2:]]
        
        # add padding to ease on calculations
        while(len(ops) != opNum):
            ops = [0] + ops

        output = nums[0]
        for on, o in enumerate(ops):
            if(o == 0):
                #add
                output += nums[on+1]
            if(o == 1):
                #add
                output *= nums[on+1]
            
        if output == res:
            return output

    return 0



    



lines = d.split("\n")

output = 0
for line in lines:
    output += solve(line)

print(output)
