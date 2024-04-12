import random
import string


class Randomizer:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.symbols = string.punctuation


    def getRandom(self, length):
        characters = self.letters + self.digits + self.symbols
        return ''.join(random.choice(characters) for _ in range(length))