n = int(input())
arr = input().split()
s = 0
for i in range(n-1):
    if int(arr[i]) < int(arr[i+1]):
        s += 1
print(s)