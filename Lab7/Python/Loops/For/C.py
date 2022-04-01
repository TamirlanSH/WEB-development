from math import sqrt

a = int(input())
b = int(input())
for i in range(a,b+1):
    if i == round(sqrt(i)) * round(sqrt(i)):
        print(i, end=" ")
