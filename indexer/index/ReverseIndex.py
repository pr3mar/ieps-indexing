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
                    if len(indices) < 2:
                        reverseIndex[token].append(
                            {"filename": name, "freq": len(indices), "indexes": ','.join(indices)})
                else:
                    reverseIndex[token] = [{"filename": name, "freq": len(indices), "indexes": ','.join(indices)}]
        return reverseIndex

    @timing
    def search(self):
        print("Searching the reverse index")
    @timing
    def writeToDb(self):
        reverseIndex = self.buildIndex()
        # makes a list of tuples like  [("word","filename","frequency","indexes")] to insert in a Posting table
        postingRecord = []
        for name, val in reverseIndex.items():
            tuples = []
            for i in val.values():
                tuples.append(i)
            tuples.insert(0, name)
            postingRecord.append(tuple(tuples))

        # inserting into the Tables
        self.db.insertWord(list(reverseIndex.keys()))
        self.db.insertPosting(postingRecord)


