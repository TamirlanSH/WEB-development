n = int(input())
arr = input().split()
s = 0
for i in range(n):
    if int(arr[i]) > 0:
        s += 1
print(s)