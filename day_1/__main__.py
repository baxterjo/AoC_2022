o=[0]
for e in open("d").readlines():
    e=e.strip()
    if e=="":
        o.append(0)
    else:
        o[-1]+=int(e)
o.sort()
print(f"{o[-1]}\n{sum(o[-3:])}")