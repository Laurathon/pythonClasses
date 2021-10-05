"""Word Finder: finds random words from a dictionary."""
import random 


class WordFinder:
    """
    finds random words in a dictionary
    """
    def __init__(self, path):
        """ initializing object, starting at number """
        file = open(path, "r")
        self.words = self.parse(file)
        self.wordCount =self.wordCount(self.words)
        print(f"Here are the words {self.words}")
        print(f"{self.wordCount} words read")
       
    def parse(self, file):
        """
        Return a word in the file
        """

        return [word.strip() for word in file]
    
    def wordCount(self, words):
        """
        Returns the number of words in a file
        """
        return len(words)
    
    def random(self):
        """ returns a random word from the word file"""
        return random.choice(self.words)
        
    ...
