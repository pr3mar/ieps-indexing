from utils import timing
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputPath, outputPath):
        super(SequantialIndex, self).__init__(inputPath, outputPath)

    @timing
    def buildIndex(self):
        print("Building a sequential index")
        # TODO

    @timing
    def search(self):
        print("Searching the sequential index")
        # TODO
