def all_variants(text):
    b = list(text)
    c = b
    print (c)
    for i in b:
        for j in c:
            res = i + j
            yield res


var = all_variants ('abc')
for value in var:
    print(value)