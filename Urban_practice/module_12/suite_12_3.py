import unittest as uni
import tests_12_3

TestSuite = uni.TestSuite()

TestSuite.addTest(uni.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
TestSuite.addTest(uni.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = uni.TextTestRunner(verbosity=2)
runner.run(TestSuite)