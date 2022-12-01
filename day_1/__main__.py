with open("d.txt") as f:
    l = f.readlines()

o = []
t = 0
for e in l:
    e = e.strip()
    if e == "":
        o.append(t)
        t = 0
    else:
        t += int(e)

o.sort()
print(f"{o[-1]}\n{sum(o[-3:])}")
