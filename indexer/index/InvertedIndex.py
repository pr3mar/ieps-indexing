from utils import timing
from db import DB
from .index import Index
from preprocess import Preprocess


class InvertedIndex(Index):
    def __init__(self, inputPath, outputPath, forceRecreate=False):
        super(InvertedIndex, self).__init__(inputPath, outputPath, forceRecreate)
        self.db = DB(outputPath, forceRecreate=forceRecreate)

    @timing
    def buildIndex(self):
        if self.db.getExists() and not self.forceRecreate:
            return
        print("Building the reverse index")
        preprocessed = Preprocess.preprocessFiles(self.inputPath, self.outputPath, self.forceRecreate)
        reverseIndex = {}
        for documentName in preprocessed:
            fileContent = preprocessed[documentName]
            for token in fileContent['tokens']:
                indices = [str(i) for i, x in enumerate(fileContent['content']) if x == token]
                posting = {"documentName": documentName, "frequency": len(indices), "indexes": ','.join(indices)}
                if token not in reverseIndex:
                    reverseIndex[token] = [posting]
                else:
                    reverseIndex[token].append(posting)
        self.__writeToDb(reverseIndex)

    @timing
    def __writeToDb(self, reverseIndex):
        # makes a list of tuples like  [("word", "filename", "frequency", "indexes", "indexes_content")] to insert in a Posting table
        postingRecord = []
        for word in reverseIndex:
            for entry in reverseIndex[word]:
                postingRecord.append(tuple([word] + list(entry.values())))
        # inserting into the Tables
        self.db.insertWord(list(reverseIndex.keys()))
        self.db.insertPosting(postingRecord)
        self.db.insertExists()

    @timing
    def search(self, query):
        """
        :param query: tokenized query
        :return: grouped postings
        """
        self.db.cursor.execute(f"""
            SELECT documentName, sum(frequency) as freq, group_concat(indexes)
            FROM Posting
            WHERE word IN ({','.join(['?']*len(query))})
            GROUP BY documentName
            ORDER BY freq DESC
        """, query)
        return self.db.cursor.fetchall()
