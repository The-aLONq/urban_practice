import unittest as uni

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

class RunnerTest(uni.TestCase):
    def test_walk(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner_2 = Runner('Test Runner')
        for _ in range(10):
            runner_2.run()

        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner('Test Runner')
        runner_4 = Runner('Test Runner')

        for _ in range(10):
            runner_3.walk()

        for _ in range(10):
            runner_4.run()

        self.assertNotEqual(runner_3, runner_4)





