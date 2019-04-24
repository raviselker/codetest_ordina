import unittest
from wordfreq import WordFrequencyAnalyzer, WordFrequency


class TestCore(unittest.TestCase):

    def test_word_freq_class(self):
        self.assertEqual(WordFrequency('time', 4).__str__(),
                         "'time' has a word frequency of 4")

    def test_word_freq_analyzer_class(self):
        with self.assertRaises(TypeError):
            WordFrequencyAnalyzer(3)

    def test_calc_high_freq(self):

        test_1 = WordFrequencyAnalyzer('The sun shines over the lake')
        self.assertEqual(test_1.calc_high_freq(), 2)

        test_2 = WordFrequencyAnalyzer('')
        self.assertEqual(test_2.calc_high_freq(), 0)

        test_3 = WordFrequencyAnalyzer('NOT not NoT nOt')
        self.assertEqual(test_3.calc_high_freq(), 4)

    def test_calc_freq_word(self):

        word_string = 'It was the best of times it was the worst of times ' \
                      'it was the age of wisdom it was the age of foolishness'

        test_1 = WordFrequencyAnalyzer(word_string)
        self.assertEqual(test_1.calc_freq_word('times'), 2)

        test_2 = WordFrequencyAnalyzer('it is time for a time-out')
        self.assertEqual(test_2.calc_freq_word('time'), 2)

        test_3 = WordFrequencyAnalyzer('')
        self.assertEqual(test_3.calc_freq_word('times'), 0)

        with self.assertRaises(TypeError):
            test_1.calc_freq_word(3)

    def test_most_freq_word(self):

        test_1 = WordFrequencyAnalyzer('The sun shines over the lake')
        self.assertEqual(test_1.calc_most_freq_words(3), [
            WordFrequency('the', 2),
            WordFrequency('lake', 1),
            WordFrequency('over', 1)])

        test_2 = WordFrequencyAnalyzer('')
        self.assertEqual(test_2.calc_most_freq_words(3), [])

    def test_get_word_freq(self):

        test_1 = WordFrequencyAnalyzer('NOT not NoT nOt')
        word_freq = test_1.get_word_freq()

        self.assertEqual(word_freq, [('not', 4)])


if __name__ == '__main__':
    unittest.main()
