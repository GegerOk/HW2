class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message

class ProcessingException(Exception):
    pass

def func(a):
    if a == 'Tarabarshina':
        raise InvalidDataException(message=(f'Нельзя писать "{a}"!' ))
    elif a == 'Гэги':
        raise ProcessingException(f'Ни в коем случае, никогда не пиши "{a}"')

try:
    func('Tarabarshina')
except InvalidDataException as inv:
    print(f'Ошибка была перехвачена, {inv.message}')
except ProcessingException as proc:
    print(f'Ошибка была перехвачена')

try:
    func('Гэги')
except InvalidDataException as inv:
    print('Ошибка была перехвачена')
except ProcessingException as proc:
    print(f'Ошибка была перехвачена')
