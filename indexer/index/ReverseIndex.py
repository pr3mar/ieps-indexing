from utils import timing
from db import DB
from .index import Index


class ReverseIndex(Index):
    def __init__(self):
        super(ReverseIndex, self).__init__()

    @timing
    def buildIndex(self):
        print("Building a reverse index")
        # TODO

    @timing
    def search(self):
        print("Searching the reverse index")
