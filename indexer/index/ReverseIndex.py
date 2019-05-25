from utils import timing
from db import DB
from .index import Index


class ReverseIndex(Index):
    def __init__(self, inputTokens, outputPath, db):
        super(ReverseIndex, self).__init__(inputTokens, outputPath, db)
        self.inputTokens = inputTokens

    @timing
    def buildIndex(self):
        print("Building a reverse index")
        reverseIndex = {}  # holds the reverse index

        for name in self.inputTokens:
            cont = self.inputTokens[name]
            for token in cont['tokens']:
                indices = [str(i) for i, x in enumerate(cont['tokens']) if x == token]
                indices_content = [str(i) for i,x in enumerate(cont['content']) if x == token]
                if token not in reverseIndex:
                    reverseIndex[token] = [
                        {"documentName": name, "frequency": len(indices), "indexes": ','.join(indices),"indexes_content":",".join(indices_content)}]
                elif token in reverseIndex:
                    if reverseIndex[token][-1]['documentName'] != name:
                        reverseIndex[token].append(
                            {"documentName": name, "frequency": len(indices), "indexes": ','.join(indices),
                             "indexes_content": ','.join(indices_content)})
        return reverseIndex


    @timing
    def search(self):
        print("Searching the reverse index")
    @timing
    def writeToDb(self):
        reverseIndex = self.buildIndex()
        # makes a list of tuples like  [("word","filename","frequency","indexes","indexes_content")] to insert in a Posting table
        postingRecord = []
        for name in reverseIndex:
            for x in reverseIndex[name]:
                temp = list(x.values())
                temp.insert(0,name)
                postingRecord.append(tuple(temp))
        # inserting into the Tables
        self.db.insertWord(list(reverseIndex.keys()))
        self.db.insertPosting(postingRecord)




