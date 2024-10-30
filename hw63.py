'''
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)'''


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                if isinstance(data, (list, tuple)):
                    file.write(' '.join(map(str, data)) + '\n')
                else:
                    file.write(str(data) + '\n') 
    return write_everything

write = get_advanced_writer('a.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



import random

class MysticBall:
    def __init__(self, words):
        self.words = words  

    def __call__(self):
        return random.choice(self.words)  


if __name__ == "__main__":
    options = [
        "Да", 
        "Нет", 
        "Возможно", 
        "Скорее всего", 
        "Не знаю", 
        "Абсолютно"
    ]
    
    magic_ball = MysticBall(options)
    
    for i in range (5):  
        result = magic_ball()  
        print(result)  
