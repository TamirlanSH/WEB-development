def min(a, b, c, d):
    if (a < b):
        if (a < c):
            if (a < d):
                return a
            else:
                return d
        elif (c < d):
            return c
        else:
            return d
    elif (b < c):
        if (b < d):
            return b
        else:
            return d
    elif (c < d):
        return c
    else:
        return d

s = input().split()
print(min(int(s[0]), int(s[1]), int(s[2]), int(s[3])))
