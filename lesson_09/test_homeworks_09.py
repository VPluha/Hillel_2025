import unittest
from homeworks import sum_two_numbers
from homeworks import average
from homeworks import longest_word
from lesson_09.homeworks import revers_text


class MyTestCase(unittest.TestCase):
    def test_for_sum(self):
        self.assertEqual(sum_two_numbers(15, 12), 27 )      # дорівнює a == b

    def test_for_sum2(self):
        self.assertNotEqual(sum_two_numbers(15, 12), 28)    # не дорівнює a != b

    def test_for_sum3(self):
        self.assertGreater(sum_two_numbers(15, 12), 20)         # більше a > b

    def test_for_sum4(self):
        self.assertLess(sum_two_numbers(15, 12), 100)           # менше a < b

    def test_for_sum5(self):
        self.assertGreaterEqual(sum_two_numbers(15, 12), 26)    # більше або дорівнює a >= b

    def test_for_sum6(self):
        self.assertLessEqual(sum_two_numbers(15, 12), 29)       # меньше або дорівнює a <= b


class AverageNumber(unittest.TestCase):
    def test_average_true_list(self):
        self.assertEqual(average([9, 6, 8, 4, 5]), 6.4)

    def test_average_true_list2(self):
        #self.assertAlmostEqual(average([9, 6, 8, 4, 5]), 6.4)
        self.assertAlmostEqual(average([-3, 3]), 0.0)                         # майже рівні

class ReversedList(unittest.TestCase):
    def test_reversed_list(self):
        input_text = "Madam, Racecar, Level, Radar, Rotor, Civic"
        expected_result = "civic ,rotor ,radar ,level ,racecar ,madam"
        self.assertEqual(revers_text(input_text), expected_result)


class LongestWord(unittest.TestCase):
    def test_longest_word(self):
        self.assertNotEqual(longest_word(["Kherson", "Bakhmut", "Enerhodar", "Mariupol"]), "Melitopol")

    def test_longest_word2(self):
        self.assertEqual(longest_word(["Kherson", "Bakhmut", "Enerhodar", "Mariupol"]), "Enerhodar")



