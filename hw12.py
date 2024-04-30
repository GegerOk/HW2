def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)
values_list_2 = ["str", 2]
values_list = [2, "STR", False]
values_dict = {'a' : 3, 'b' : "string", 'c' : False}
#print_params(23, 17, 11, 19)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)