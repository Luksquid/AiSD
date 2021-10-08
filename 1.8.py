def foo():
    l = []
    for i in range(3):
        l.append(int(input()))
    return tuple(l)
print(foo())
