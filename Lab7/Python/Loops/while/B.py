a = int(input())
i = 2
minA = a
while i <= a:
    if(a % i == 0) and (i < minA):
        minA = i
    i += 1
print(minA)