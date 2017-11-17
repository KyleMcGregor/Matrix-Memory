from random import randint
from datetime import datetime

class Game:
    """Abstraction to represent the gameboard array and question attempt model"""

    def __init__(self, rows: int, cols: int, minval: int, maxval: int):
        self.rows = rows
        self.cols = cols
        self.minval = minval
        self.maxval = maxval
        self.attempts = list()
        self.questions = list()

    def make_question(self) -> list:
        return [[randint(self.minval, self.maxval) for x in range(0,self.rows)] for x in range(0, self.cols)]

    def make_attempt(self, att: list) -> bool:
        """Log the time the attempt was made and the full data of the attempt"""
        self.attempts.append({datetime.now(): att})

    def enabled_list(self) -> list:
        """return a bit matrix indicating whcih items in the UI game board should be enabled"""
        enld = list()
        for r in range(0, self.rows):
            for c in range(0, self.cols):
                if (r <= self.rows and c <= self.cols):
                    enld.append({(r,c):True})


    def __delslice__(self, i, j):
        pass

    def __getitem__(self, item):
        pass

    def __