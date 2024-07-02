def operation(first_obj, second_obj, opp):
    if opp == "-":
        return first_obj - second_obj
    elif opp == "+":
        return first_obj + second_obj
    
result = operation(1,2,"+")
print (result)

myltiply = lambda x, y: x * y
print (myltiply(3, 4))

class Repeater:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return [self.value] * n

repeat_five = Repeater(5)
print(repeat_five(5))