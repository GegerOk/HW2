def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None
    total_sum, incorrect_data = personal_sum(numbers)
    try:
        average = total_sum / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    return average


print(personal_sum([1, 2, 3, 'a', 4, None]))
print(calculate_average([1, 2, 3, 'a', 4, None]))
print(calculate_average(123))
print(calculate_average([]))
