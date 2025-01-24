import unittest as uni
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename=' runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
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

class RunnerTest(uni.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Test Runner')
            runner.speed = -abs(runner.speed)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')


    def test_run(self):
        try:
            runner_2 = Runner('Test Runner', -5)
            for _ in range(10):
                runner_2.run()

            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    def test_challenge(self):
        runner_3 = Runner('Test Runner')
        runner_4 = Runner('Test Runner')

        for _ in range(10):
            runner_3.walk()

        for _ in range(10):
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())

if __name__ == '__main__':
    uni.main()