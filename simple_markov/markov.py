""" This module contains a class for generating markov strings. """
import random
import re

class Markov():
    """ This class remembers a corpus of text and generates markov strings. """

    def __init__(self, text):
        self.text = text

    def generate(self):
        """ This method generates markov strings. """
        blobs = [blob for blob in self.text.split('\n') if blob]
        word = re.escape(random.choice(blobs).split(' ')[0])
        sentence = word
        still_chuggin = True
        while still_chuggin:
            matches = [(m.start(0), m.end(0)) for m in re.finditer(word + " ", self.text)]
            if matches:
                match = random.choice(matches)
                word = self.text[match[0]:].split(' ')[1]
                if "\n" in word:
                    still_chuggin = False
                sentence = sentence + " " + word.split('\n')[0]
            else:
                still_chuggin = False

        return sentence.replace('\\', '')

    def add_text(self, text):
        """ This method is for when you wanna add text and don't wanna reinstanciate """
        self.text = self.text + "\n" + text
