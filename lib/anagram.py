# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for candidate in words:
            if sorted(candidate.lower()) == sorted(self.word.lower()) and candidate.lower() != self.word.lower():
                anagrams.append(candidate)
        return anagrams