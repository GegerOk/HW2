def is_prime(func):
    def wrapper( * args):
        result = func( * args)
        a = 2
        while a != result:
            a += 1
            if result % a == 0:
                return 'Составное'
            else:
                return 'Простое'
    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third

result = sum_three(2, 4, 5)
print(result)
