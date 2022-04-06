n = int(input())

m = input().split()
s = 0
for i in range(1, n-1):
    if(int(m[i]) > int(m[i-1]) and int(m[i]) > int(m[i+1])):
        s = s + 1
print(s)