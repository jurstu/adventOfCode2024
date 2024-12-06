


with open("input", "r") as f:
    d = f.read()

rules, pages = d.split("\n\n")

print(rules)
print(pages)

rr = {}

for line in rules.split("\n"):
    a,b = line.split("|")
    if(not a in rr):
        rr[a] = [b]
    else:
        rr[a].append(b)





mult = []

for line in pages.split("\n"):
    isGood = 1
    out = 0
    numbers = line.split(",")
    #print(numbers)
    for i, testing in enumerate(numbers):
        toCheck = numbers[i+1:]
        #print(f"for number {testing} i will check {toCheck}")
        for rest in (toCheck):
            #print(f"checking {rest}")
            if(f"{rest}" in rr):
                arr = rr[f"{rest}"]

                if(testing in arr):
                    isGood = 0
                    out = 1


            if(out):
                break
        if(out):
            break
    if(isGood == 0):
        
        mult.append(numbers)
    out = 0

print(mult) # wrong orderings of pages


def testLine(numbers):
    for i, testing in enumerate(numbers):
        toCheck = numbers[i+1:]
        for j, rest in enumerate(toCheck):
            if(f"{rest}" in rr):
                arr = rr[f"{rest}"]

                if(testing in arr):
                    return i, j+i+1
    return "good"


OUTPUT = 0

for line in mult:
    isGood = 1
    out = 0
    numbers = line

    res = 1
    print("correcting", numbers)
    while (res):
        out = testLine(numbers)
        if(type(out) == str):
            res = 0
        else:
            i, j = out
            print(f"swapping {i} {j}")
            a = numbers[i]
            b = numbers[j]
            numbers[j] = a
            numbers[i] = b
        
    print("GOOD", numbers)
    OUTPUT += int(numbers[int(len(numbers)/2)])

print(OUTPUT)
   