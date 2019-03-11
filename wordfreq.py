import re

class IWordFrequency():

    def WordFrequency(wordstring):

        # split string into words
        wordlist = re.split('[^a-zA-Z]', wordstring.lower())
        wordlist = list(filter(None, wordlist))

        # add word frequencies and make dictionary
        wordfreq = [(p, wordlist.count(p)) for p in wordlist]
        freqdict = dict(wordfreq)

        return freqdict


class IWordFrequencyAnalyzer():

    def CalculateHighestFrequency(wordstring):

        freqdict = IWordFrequency.WordFrequency(wordstring)

        # return the largest frequency
        if freqdict:
            return freqdict[max(freqdict, key=freqdict.get)]
        else:
            return 0

    def CalculateFrequencyForWord(wordstring, word):

        freqdict = IWordFrequency.WordFrequency(wordstring)

        # return frequency of word
        if word in freqdict:
            return freqdict[word]
        else:
            return 0

    def CalculateMostFrequentNWords(wordstring, n):

        freqdict = IWordFrequency.WordFrequency(wordstring)

        # make list and sort
        freqdictsorted = [(key, freqdict[key]) for key in freqdict]
        freqdictsorted.sort(key = lambda l: (-l[1], l[0]))

        # return 1:n highest frequency words
        return freqdictsorted[:n]
