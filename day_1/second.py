


with open("input", "r") as f:
    d = f.read()

lines = d.split("\n")
pairs = [[int(x.split(" ")[0]), int(x.split(" ")[-1])] for x in lines]


lists = [[x[0] for x in pairs], [x[1] for x in pairs]]
lists[0].sort()
lists[1].sort()

output = 0
for a in lists[0]:
    output += a * lists[1].count(a)

print(output)


