from utils import timing
from db import DB
from .index import Index


class ReverseIndex(Index):
    def __init__(self, inputTokens, outputPath, db):
        super(ReverseIndex, self).__init__(inputTokens, outputPath, db)

    @timing
    def buildIndex(self):
        print("Building a reverse index")
        reverseIndex = {} # holds the revers index
        for file in self.inputTokens:
            fileName = file.fileName
            for token in file.tokens:
                pass
                # todo: if exists -> update
                # if not -> add
                # reverseIndex[token]
        # TODO
        #   insert into Sqlite
        #   AT MOST 2 INSERTS

    @timing
    def search(self):
        print("Searching the reverse index")
