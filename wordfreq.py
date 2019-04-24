import re
from collections import Counter


class WordFrequency:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __str__(self):
        return f"'{self.word}' has a word frequency of {self.freq}"

    def __eq__(self, other):
        return self.word == other.word and self.freq == other.freq

    def __lt__(self, other):
        return (
            self.word > other.word
            if self.freq == other.freq
            else self.freq < other.freq
        )


class WordFrequencyAnalyzer:

    __word_freq = []

    def __init__(self, text: str):
        # check whether text is a string
        if not isinstance(text, str):
            raise TypeError('input should be of type string')

        # split string into words
        word_list = re.split('[^a-zA-Z]', text.lower())
        word_list = list(filter(None, word_list))

        # get word freq
        self.__word_freq = Counter(word_list).most_common()

    def calc_high_freq(self) -> int:
        """
        Return the highest word frequency of a string.
        :returns: integer: highest frequency
        """
        if self.__word_freq:
            return self.__word_freq[0][1]
        else:
            return 0

    def calc_freq_word(self, word: str) -> int:
        """
        Return the word frequency of a word in a string.
        :param String word: The word for which the frequency needs to be
        returned
        :returns: integer: frequency of 'word'
        """
        # check whether word is a string
        if not isinstance(word, str):
            raise TypeError('\'word\' should be of type string')

        if word in dict(self.__word_freq):
            return dict(self.__word_freq)[word]
        else:
            return 0

    def calc_most_freq_words(self, n: int):
        """
        Return the most frequent n words in a string.
        :param integer n: The number of word frequencies that need to be
        returned
        :returns: a list of WordFrequency objects
        """
        word_freq_list = [WordFrequency(word, freq)
                          for word, freq in self.__word_freq]
        return sorted(word_freq_list, reverse=True)[:n]

    def get_word_freq(self):
        """Return a list of word frequencies."""
        return self.__word_freq
