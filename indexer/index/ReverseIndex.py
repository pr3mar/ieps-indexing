from utils import timing
from db import DB
from .index import Index


class ReverseIndex(Index):
    def __init__(self, inputTokens, outputPath, db):
        super(ReverseIndex, self).__init__(inputTokens, outputPath, db)

    @timing
    def buildIndex(self):
        print("Building a reverse index")
        reverseIndex = {}  # holds the revers index

        for fajl in self.inputTokens:
            name = fajl['fileName']
            for token in fajl['tokens']:
                indices = [i for i, x in enumerate(fajl["tokens"]) if x == token]
                if token in reverseIndex:
                    if fajl['tokens'].count(token) < 2:
                        reverseIndex[token].append(
                            {"filename": name, "freq": fajl['tokens'].count(token), "indexes": indices})
                else:
                    reverseIndex[token] = [{"filename": name, "freq": 0, "indexes": indices}]
        return reverseIndex

    @timing
    def search(self):
        print("Searching the reverse index")
