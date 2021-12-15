import unittest

import binary_diagnostic


class TestSonarSweep(unittest.TestCase):
    def test_split_binary_vertically(self):
        self.assertEqual(binary_diagnostic.split_binary_vertically(['00100',
                                                                    '11110',
                                                                    '10110',
                                                                    '10111',
                                                                    '10101']), [
                             '01111', '01000', '11111', '01110', '00011'
                         ])

    def test_find_o2(self):
        self.assertEqual(binary_diagnostic.find_o2(['00100',
                                                    '11110',
                                                    '10110',
                                                    '10111',
                                                    '10101',
                                                    '01111',
                                                    '00111',
                                                    '11100',
                                                    '10000',
                                                    '11001',
                                                    '00010',
                                                    '01010']),
                         '10111')

    def test_find_co2(self):
        self.assertEqual(binary_diagnostic.find_co2(['00100',
                                                     '11110',
                                                     '10110',
                                                     '10111',
                                                     '10101',
                                                     '01111',
                                                     '00111',
                                                     '11100',
                                                     '10000',
                                                     '11001',
                                                     '00010',
                                                     '01010']),
                         '01010')

    def test_common_binary(self):
        self.assertEqual(binary_diagnostic.common_binary([
            '01111', '01000', '11111', '01110', '00011'
        ]), '10110')

    def test_least_common_binary(self):
        self.assertEqual(binary_diagnostic.least_common_binary([
            '01111', '01000', '11111', '01110', '00011'
        ]), '01001')

    def test_binary_to_int(self):
        self.assertEqual(binary_diagnostic.binary_to_int('10110'), 22)
        self.assertEqual(binary_diagnostic.binary_to_int('01001'), 9)


if __name__ == '__main__':
    unittest.main()
