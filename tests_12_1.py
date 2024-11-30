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
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = Runner(name='ran1')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)
    def test_run(self):
        runner2 = Runner(name='ran2')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)
    def test_challenge(self):
        runner_1 = Runner(name='ran1')
        runner_2 = Runner(name='run2')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
