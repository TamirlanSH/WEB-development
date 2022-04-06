n = int(input())
arr = input().split()
s = 0
for i in range(n-1):
    if (int(arr[i]) > 0 and int(arr[i+1]) > 0) or (int(arr[i]) < 0 and int(arr[i+1]) < 0):
        s += 1
if s > 0:
    print("YES")
else:
    print("NO")