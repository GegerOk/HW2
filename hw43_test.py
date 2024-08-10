import unittest
import hw43
import hw41
all_tests = unittest.TestSuite()
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(hw43.TournamentTest))
all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(hw43.Test_Runner))
final_test = unittest.TextTestRunner(verbosity=2)
final_test.run(all_tests)