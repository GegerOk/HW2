my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
answer = [x ** 2 for x in my_list if x % 2]
print (answer)

def fil (x):
    return x % 2

def mlp (x):
    return x ** 2

answer = filter (fil, my_list)
answer = map (mlp, answer)
print (list (answer))