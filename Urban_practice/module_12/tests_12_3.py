import unittest as uni

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

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


class RunnerTest(uni.TestCase):
    is_frozen = False

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Test Runner')
        for _ in range(10):
            runner_2.run()

        self.assertEqual(runner_2.distance, 100)

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Test Runner')
        runner_4 = Runner('Test Runner')

        for _ in range(10):
            runner_3.walk()

        for _ in range(10):
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


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

class TournamentTest(uni.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner('Усейн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f'{test_name}: {result}')

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_nick(self):
        #забег усэйна и ника
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.all_results["test_tournament_usain_nick"] = results

        last_palce = max(results.keys())
        self.assertTrue(results[last_palce].name == 'Ник')

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrey_nick(self):
        #забег андрея и ника
        tournament= Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.all_results['test_tournament_andrey_nick'] = results

        last_palce = max(results.keys())
        self.assertTrue(results[last_palce].name == 'Ник')

    @uni.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_all_runners(self):
        #забег всех троих
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.all_results['test_tournament_all_runners'] = results

        last_palce = max(results.keys())
        self.assertTrue(results[last_palce].name == 'Ник')

if __name__ == "__main__":
    uni.main()

