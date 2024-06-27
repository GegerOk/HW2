file_name = 'new.txt'
with open(file_name, mode = 'r', encoding = 'utf8') as file:
    for line in file:
        print(line)
# Если я правильно понял, оператор with сам закрывает файл, после конца работы с ним