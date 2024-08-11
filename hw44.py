import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format= '%(asctime)s / %(levelname)s / %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

class Test_Runner(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        try:
            speed = Runner('Sala', 5)
            for i in range (10):
                speed.walk()
            self.assertEqual(speed.distance, 50)
            logging.info('walk выполнено успешно')
        except:
            logging.warning('Произошла ошибка в блоке walk', exc_info=True)

    def test_run(self):
        try:
            Nspeed = Runner('NSala', -5)
            for i in range (10):
                Nspeed.run()
            self.assertEqual(Nspeed.distance, 100)
            logging.info('run выполнено успешно')
        except:
            logging.warning('Произошла ошибка в блоке run', exc_info=True)

    @unittest.skipIf(is_frozen, reason = 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        f_run = Runner('1_run', 5)
        s_run = Runner('2_run', 5)
        for i in range (10):
            f_run.walk()
            s_run.run()
        self.assertNotEqual(f_run.distance, s_run.distance)

if __name__ == '__main__':
    unittest.main()