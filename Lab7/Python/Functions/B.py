def power(a, n):
    return a**n

s = input().split()
print(power(float(s[0]), int(s[1])))