import unittest

import submarine


class TestSonarSweep(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(submarine.parse_value('5'), 5)
        self.assertEqual(submarine.parse_value('15'), 15)

    def test_split_values(self):
        self.assertEqual(submarine.split_values(['forward 5']), [['forward', 5]])
        self.assertEqual(submarine.split_values(['down 5']), [['down', 5]])

    def test_count_increase(self):
        self.assertEqual(
            submarine.count_increase(
                [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]),
            {"horizontalPosition": 15, "depth": 60})


if __name__ == '__main__':
    unittest.main()
