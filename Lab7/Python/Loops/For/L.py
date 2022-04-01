a = input()
s = 0
for i in range(len(a)):
    s = s + int(a[i]) * 2**(len(a)- 1 - i)
print(s)