import unittest

import sonar_sweep


class TestSonarSweep(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(sonar_sweep.parse_values(['5']), [5])
        self.assertEqual(sonar_sweep.parse_values(['15', 55, '8']), [15, 55, 8])

    def test_count_increases(self):
        self.assertEqual(sonar_sweep.count_increases([607, 618, 618, 617, 647, 716, 769, 792]), 5)

    def test_convert_to_3d(self):
        self.assertEqual(sonar_sweep.convert_to_3d([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]), [
            [199, 200, 208],
            [200, 208, 210],
            [208, 210, 200],
            [210, 200, 207],
            [200, 207, 240],
            [207, 240, 269],
            [240, 269, 260],
            [269, 260, 263]
        ])

    def test_sum_3d_values(self):
        self.assertEqual(sonar_sweep.sum_3d_values([[199, 200, 208],
                                                    [200, 208, 210],
                                                    [208, 210, 200],
                                                    [210, 200, 207],
                                                    [200, 207, 240],
                                                    [207, 240, 269],
                                                    [240, 269, 260],
                                                    [269, 260, 263]]), [607, 618, 618, 617, 647, 716, 769, 792])


if __name__ == '__main__':
    unittest.main()
