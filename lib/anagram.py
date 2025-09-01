# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for consistent comparison
    
    def match(self, possible_anagrams):
        # Return a list of words from possible_anagrams that are actual anagrams
        return [candidate for candidate in possible_anagrams 
                if self._is_anagram(candidate)]
    
    def _is_anagram(self, candidate):
        # Helper method to check if a candidate word is an anagram
        candidate = candidate.lower()
        # A word is not an anagram of itself
        if candidate == self.word:
            return False
        # Compare sorted letters of both words
        return sorted(self.word) == sorted(candidate)