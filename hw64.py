def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            byte_position = file.tell()
            file.write(string + '\n')
            strings_positions[(index + 1, byte_position)] = string
    return strings_positions


file_name = 'output.txt'
strings = ['Hello, world!', 'This is a test.', 'Test 2.']
result = custom_write(file_name, strings)
print(result)
