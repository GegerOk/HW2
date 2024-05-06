def test(a):
    if a == 1:
        return a
    else:
        return a * test(a - 1)
print (test(15))