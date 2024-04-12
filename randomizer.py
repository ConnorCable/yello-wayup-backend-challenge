import random
import string


class Randomizer:
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits

    def getRandom(self, length):
        characters = self.letters + self.digits
        return ''.join(random.choice(characters) for _ in range(length))
