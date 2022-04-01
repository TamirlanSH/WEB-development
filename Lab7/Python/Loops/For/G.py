
# Online Python - IDE, Editor, Compiler, Interpreter
x = int(input())
s = x
for i in range(2, x):
    if (x % i == 0) and (i < s):
        s = i
print(s)
