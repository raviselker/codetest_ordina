import re
from collections import Counter


class WordFrequency:

    def word(self):
        pass

    def frequency(self):
        pass


class WordFrequencyAnalyzer:

    __word_freq_sorted = None

    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError('input should be of type string')

        # split string into words
        word_list = re.split('[^a-zA-Z]', text.lower())
        word_list = list(filter(None, word_list))

        # get word freq and sort by frequency + alphabetical
        word_freq = Counter(word_list).most_common()
        self.__word_freq_sorted = sorted(word_freq, key=lambda l: (-l[1], l[0]))

    def calc_high_freq(self):
        """Return the highest word frequency of a string."""
        if self.__word_freq_sorted:
            return self.__word_freq_sorted[0][1]
        else:
            return 0

    def calc_freq_word(self, word):
        """Return the word frequency of a word in a string."""
        if word in dict(self.__word_freq_sorted):
            return dict(self.__word_freq_sorted)[word]
        else:
            return 0

    def calc_most_freq_word(self, n):
        """Return the most frequent n words in a string."""
        return self.__word_freq_sorted[:n]

    def get_word_freq(self):
        """Return a list of word frequencies."""
        return self.__word_freq_sorted
