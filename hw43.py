import unittest
import pprint

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
        self.finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    self.finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return self.finishers

class Test_Runner(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        speed = Runner('Sala', 5)
        for i in range (10):
            speed.walk()
        self.assertEqual(speed.distance, 50)

    def test_run(self):
        Nspeed = Runner('NSala', 5)
        for i in range (10):
            Nspeed.run()
        self.assertEqual(Nspeed.distance, 100)

    @unittest.skipIf(is_frozen, reason = 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        f_run = Runner('1_run', 5)
        s_run = Runner('2_run', 5)
        for i in range (10):
            f_run.walk()
            s_run.run()
        self.assertNotEqual(f_run.distance, s_run.distance)
    
class TournamentTest (unittest.TestCase):
    global is_frozen
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []
    
    def setUp(self):
        self.usain = Runner(name = 'Usain', speed = 10)
        self.andrey = Runner(name = 'Andrey', speed = 9)
        self.nick = Runner(name = 'Nick', speed = 3)
        return self.usain, self.andrey, self.nick

    @classmethod
    def tearDownClass(cls):
        pprint.pprint (all_results)
        
    @unittest.skipIf(is_frozen, reason = 'Тесты в этом кейсе заморожены')
    def test_1(self):
        t1 = Tournament(90, self.usain, self.nick)
        t1.start()
        all_results.append (t1.finishers)
        keys = list(t1.finishers.keys())
        last_finisher = keys [-1]
        self.assertTrue(last_finisher, 'Nick')

        t2 = Tournament(90, self.andrey, self.nick)
        t2.start()
        all_results.append (t2.finishers)
        keys = list(t2.finishers.keys())
        last_finisher = keys [-1]
        self.assertTrue(last_finisher, 'Nick')

        t3 = Tournament(90, self.usain, self.andrey, self.nick)
        t3.start()
        all_results.append (t3.finishers)
        keys = list(t3.finishers.keys())
        last_finisher = keys [-1]
        self.assertTrue(last_finisher, 'Nick')

if __name__ == '__main__':
    unittest.main()