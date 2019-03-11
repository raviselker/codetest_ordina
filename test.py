import unittest
from wordfreq import WordFrequencyAnalyzer


class TestCore(unittest.TestCase):

    def test_calc_high_freq(self):

        word_string = 'The sun shines over the lake'

        test_1 = WordFrequencyAnalyzer.calc_high_freq(word_string)
        self.assertEqual(test_1, 2)

        test_2 = WordFrequencyAnalyzer.calc_high_freq('')
        self.assertEqual(test_2, 0)

        test_3 = WordFrequencyAnalyzer.calc_high_freq('NOT not NoT nOt')
        self.assertEqual(test_3, 4)

    def test_calc_freq_word(self):

        word_string = 'It was the best of times it was the worst of times ' \
                      'it was the age of wisdom it was the age of foolishness'

        test_1 = WordFrequencyAnalyzer.calc_freq_word(word_string, 'times')
        self.assertEqual(test_1, 2)

        test_2 = WordFrequencyAnalyzer.calc_freq_word('it is time for a time-out', 'time')
        self.assertEqual(test_2, 2)

        test_3 = WordFrequencyAnalyzer.calc_freq_word('', 'time')
        self.assertEqual(test_3, 0)

    def test_most_freq_word(self):

        word_string = 'The sun shines over the lake'

        test_1 = WordFrequencyAnalyzer.calc_most_freq_word(word_string, 3)
        self.assertEqual(test_1, [('the', 2), ('lake', 1), ('over', 1)])

        test_2 = WordFrequencyAnalyzer.calc_most_freq_word('', 2)
        self.assertEqual(test_2, [])


if __name__ == '__main__':
    unittest.main()
