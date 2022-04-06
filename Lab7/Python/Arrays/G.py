n = int(input())
m = input().split()
k = ''
for i in range(n//2):
    k = m[i]
    m[i] = m[n-i-1]
    m[n-i-1] = k
for i in range(n):
    print(int(m[i]),end=" ")