def foo(lit, naz):
    return lit.capitalize() + '.' + naz.capitalize()
def fo2(imie, nazwisko, func):
    return func(imie, nazwisko) + " - informatyk"
print(fo2("l", "kalamarski", foo))
