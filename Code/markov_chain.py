import random

class MarkovChain(dict):
        def __init__(self, word_list=None):
            super(MarkovChain, self).__init__()  # Initialize this as a new list
            corpus = open("Code/fox.txt", "r")
            # Add properties to track useful word counts for this histogram
            self.types = 0  # Count of distinct word types in this histogram
            self.tokens = 0  # Total count of all word tokens in this histogram
            # Count words in given list, if any
            if word_list is not None:
                self.add_count(word_list)
    
        def search(self, word):
            """Looks for a word in the listogram. Return None if not found."""
            for index, word_and_count in enumerate(self):
                if word_and_count[0] == word:
                    return word, index
            return None, 0
    
        def add_count(self, word_list):
            """Increase frequency count of given word by given count amount."""
            