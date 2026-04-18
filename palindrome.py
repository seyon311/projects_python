def pal(t):
    s = len(t)-1
    e = 0
    while s > e:
        if t[s] != t[e]:
            return False
        s -= 1
        e += 1
    return True

tuple1 = (1, 2, 3, 3, 2, 1)

print(pal(tuple1))
