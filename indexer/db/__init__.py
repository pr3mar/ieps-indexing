import sqlite3
from utils import timing

# TODO handle sqlite
class DB(object):

    # TODO:
    #   - connect to database
    #   - create if not created
    #   - select from table <>
    #   - write into table <>
    #   - update table
    #   - truncate database
    def __init__(self, inputPath, dbName = "indexer"):
        pass

    def getWord(self, word):
        pass
        # TODO: execute query on Word table
