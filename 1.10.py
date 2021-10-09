from math import *
def foo(l):
    for i in range(0, floor(len(l) / 2)):
        if l[i] != l[len(l) - 1 - i]:
            return False
        if i == floor(len(l) / 2) - 1:
            return True
print(foo("12321"))
