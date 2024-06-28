import random

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """Machine for generating random words from a dictionary file. 
    
     >>> wf = WordFinder("Users/student/words.txt")
     3 words read

     >>> wf.random()
     'cat'

     >>> wf.random()
     'cat'

     >>> wf.random()
     'porcupine'

     >>> wf.random()
     'dog'
       """
    
    def __init__(self , file_path):
        """Read dictionary and report number of words read."""

        # open dictionary file.
        dict_file = open(file_path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")
    

    def parse(self , dict_file):
        """parse each word in dictionary file list of words"""

        return [word.strip() for word in dict_file]
    

    def random(self):
        """Return random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special class that extends from WordFinder. This class will never return the blank lines and comments.

    >>> swf = SpecialWordFinder("Users/student/Vegetables&Fruits.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self , dict_file):

        return [ word.strip() 
                for word in dict_file 
                if word.strip() and not word.startswith('#')]