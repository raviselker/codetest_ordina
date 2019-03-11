import unittest
from wordfreq import IWordFrequencyAnalyzer

class TestCore(unittest.TestCase):

    def test_wordfreq(self):

        wordstring = 'It was, the best of times it was the worst of times '
        wordstring += 'it was the age of wisdom it was the age of foolishness'

        t1 = IWordFrequencyAnalyzer.CalculateHighestFrequency(wordstring)
        t2 = IWordFrequencyAnalyzer.CalculateFrequencyForWord(wordstring, 'times')
        t3 = IWordFrequencyAnalyzer.CalculateMostFrequentNWords(wordstring, 3)
        t4 = IWordFrequencyAnalyzer.CalculateHighestFrequency('')
        t5 = IWordFrequencyAnalyzer.CalculateMostFrequentNWords('', 2)
        t6 = IWordFrequencyAnalyzer.CalculateFrequencyForWord('it is time for a time-out', 'time')
        t7 = IWordFrequencyAnalyzer.CalculateHighestFrequency('NOT not NoT nOt')

        self.assertEqual(t1, 4)
        self.assertEqual(t2, 2)
        self.assertEqual(t3[2], ('the', 4))
        self.assertEqual(t4, 0)
        self.assertEqual(t5, [])
        self.assertEqual(t6, 2)
        self.assertEqual(t7, 4)

if __name__ == '__main__':
    unittest.main()
