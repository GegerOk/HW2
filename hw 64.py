def apply_all_func(int_list, *functions):
    results = {}  
    for func in functions:  
        results[func.__name__] = func(int_list)  
    return results  


if __name__ == "__main__":
    int_list = [1, 2, 3, 4, 5, -1, 0.5]
    result = apply_all_func(int_list, min, max, len, sum, sorted)
    print(result)
