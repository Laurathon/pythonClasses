from wordfinder import WordFinder

class RandomWord(WordFinder):
  """ special random word """

  
  def __init__(self, path):
    """ initializing object, starting at number """
    file = open(path, "r")
    self.words = self.parse(file)
    print(f"new words are {self.words}")
   
    
  def parse(self, file):
        """
        Return a word in the file with no spaces, line returns or #
        """
        x=[]
    
        x = [word.strip() for word in file if not word.startswith("#")]
        while '' in x:
          x.remove('')
        return x
  
     
       
