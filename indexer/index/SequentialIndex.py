from utils import timing
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputTokens, outputPath, db):
        super(SequantialIndex, self).__init__(inputTokens, outputPath, db)

    @timing
    def buildIndex(self):
        print("Building a sequential index")
        # TODO

    @timing
    def search(self):
        print("Searching the sequential index")
        # TODO
