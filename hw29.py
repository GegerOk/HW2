class ProceedException (Exception):
    def wrong_word(a):
        try:
            if a == 'Tarabarshina':
                raise Exception (f'Нельзя писать "{a}"!')
        except ProceedException as e:
            print('Возникла ошибка {e}, но была перехвачена')

Pro = ProceedException
Pro.wrong_word ('Tarabarshina')

class InvalidDataException (Exception):
    def wrong_word(a):
        try:
            if a == 'Гэги':
                raise Exception (f'Нельзя писать "{a}"!')
        except InvalidDataException as e:
            print('Возникла ошибка {e}, но была перехвачена')

Inv = InvalidDataException
Inv.wrong_word ('Гэги')
