t="ABC"
y="XYZ"
s = 0
for m in open("d").readlines():
    c = y.index(m[2])
    r = abs(c-t.index(m[0]))