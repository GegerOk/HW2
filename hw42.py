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

    
class TournamentTest (unittest.TestCase):
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
    
    def test(self):
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