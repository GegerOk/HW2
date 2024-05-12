def test(a):
    if a == 1:
        return a
    else:
        return a * test(a - 1)
print (test(15))
def test_2(*params):
    print (params)
test_2(1, 2, "a", True)
