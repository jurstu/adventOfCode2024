


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
    if(isGood):
        print("good", numbers)
        mult.append(int(numbers[int(len(numbers)/2)]))
    out = 0

print(mult)

out = sum(mult)
print(out)