from math import sqrt

n = int(input())
i = 1
while i <= n:
    if(i == round(sqrt(i))*round(sqrt(i))):
        print(i)
    i = i + 1