def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError as e:
        return f"{a}{b}"


a = 10  
b = 13  
print(add_everything_up(a, b))  

a = 10  
b = "Строка"  
print(add_everything_up(a, b))
