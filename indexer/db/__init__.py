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
            self.c.executescript('''
                        CREATE TABLE IndexWord (
                            word TEXT PRIMARY KEY
                                        );
                        CREATE TABLE Posting (
                            word TEXT NOT NULL,
                            documentName TEXT NOT NULL,
                            frequency INTEGER NOT NULL,
                            indexes TEXT NOT NULL,
                            PRIMARY KEY(word, documentName),
                            FOREIGN KEY (word) REFERENCES IndexWord(word)
                                ); 
                            CREATE TABLE Existing(doesExist BOOLEAN NOT NULL CHECK (doesExist IN (0,1)));''')
            self.conn.commit()
        except Exception as err:
            print("Database creation failed: {}".format(str(err)))

        def insertWord(self, lista):
            try:
                for item in lista:
                    self.c.execute("INSERT INTO IndexWord(word) VALUES(?)", [item])
                self.conn.commit()
            except Exception as err:
                print('Inserting into IndexWord table failed : {}'.format(str(err)))

        def insertPosting(self, postlist):
            try:
                for item in postlist:
                    self.c.execute("INSERT INTO Posting(word,documentName,frequency,indexes) VALUES(?,?,?,?)", item)
                self.conn.commit()
            except Exception as err:
                print('Inserting into Posting table failed : {}'.format(str(err)))

        #exists("0","1")
        def insertExists(self, exists):
            try:
                self.c.execute("INSERT INTO Existing(doesExist) VALUES (?)", exists)
                self.conn.commit()
            except Exception as err:
                print("Inserting into Existing table failed : {}".format(str(err)))

        def getExists(self):
            try:
                self.c.execute("SELECT * FROM Existing")
                self.conn.commit()
                return True if int(self.c.fetchone()[0]) else False
            except Exception as err:
                print("Query failed {}".format(err))


