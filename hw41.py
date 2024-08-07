import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
    
class Test_Runner(unittest.TestCase):
    def test_walk(self):
        speed = Runner('Sala')
        for i in range (10):
            speed.walk()
        self.assertEqual(speed.distance, 50)

    def test_run(self):
        Nspeed = Runner('NSala')
        for i in range (10):
            Nspeed.run()
        self.assertEqual(Nspeed.distance, 100)

    def test_challenge(self):
        f_run = Runner('1_run')
        s_run = Runner('2_run')
        for i in range (10):
            f_run.walk()
            s_run.run()
        self.assertNotEqual(f_run.distance, s_run.distance)

if __name__ == '__main__':
    unittest.main()