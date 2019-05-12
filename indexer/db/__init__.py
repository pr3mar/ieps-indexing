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

    #inicijalizacija uspjesna
    def __init__(self, inputPath, dbName = "indexer"):
        # konekcija na bazu
        conn = sqlite3.connect(inputPath + dbName)
        # pravljenje tabela
        c = conn.cursor()
        try:
            c.execute('''
                    CREATE TABLE IndexWord (
                        word TEXT PRIMARY KEY
                                    );
                        ''')
            c.execute(''' CREATE TABLE Posting (
                        word TEXT NOT NULL,
                        documentName TEXT NOT NULL,
                        frequency INTEGER NOT NULL,
                        indexes TEXT NOT NULL,
                        PRIMARY KEY(word, documentName),
                        FOREIGN KEY (word) REFERENCES IndexWord(word)
                            ); 
                        ''')
            c.executescript(''' 
                        CREATE TABLE existing(doesExist BOOLEAN NOT NULL CHECK (doesExist IN (0,1)));''')
        except:
            print('Database already exists')






