import re


class WordFrequency:

    def word_freq(self):
        """Return word frequency of all words in a string"""
        if not isinstance(self, str):
            raise TypeError('\'self\' should be of type string')

        # split string into words
        word_list = re.split('[^a-zA-Z]', self.lower())
        word_list = list(filter(None, word_list))

        # add word frequencies and make dictionary
        word_freq = [(p, word_list.count(p)) for p in word_list]
        freq_dict = dict(word_freq)

        return freq_dict


class WordFrequencyAnalyzer:

    def calc_high_freq(self):
        """Return the highest word frequency of a string."""
        if not isinstance(self, str):
            raise TypeError('\'self\' should be of type string')

        freq_dict = WordFrequency.word_freq(self)

        # return the largest frequency
        if freq_dict:
            return freq_dict[max(freq_dict, key=freq_dict.get)]
        else:
            return 0

    def calc_freq_word(self, word):
        """Return the word frequency of a word in a string."""
        if not isinstance(self, str):
            raise TypeError('\'self\' should be of type string')

        freq_dict = WordFrequency.word_freq(self)

        # return frequency of word
        if word in freq_dict:
            return freq_dict[word]
        else:
            return 0

    def calc_most_freq_word(self, n):
        """Return the most frequent n words in a string."""
        if not isinstance(self, str):
            raise TypeError('\'self\' should be of type string')

        freq_dict = WordFrequency.word_freq(self)

        # make list and sort
        freq_dict_sorted = [(key, freq_dict[key]) for key in freq_dict]
        freq_dict_sorted.sort(key=lambda l: (-l[1], l[0]))

        # return 1:n highest frequency words
        return freq_dict_sorted[:n]
