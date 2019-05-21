import sqlite3,os.path
from utils import timing

# TODO handle sqlite
class DB(object):


    def __init__(self, inputPath, dbName = "indexer.db"):
        dbPath = os.path.join(inputPath,dbName)
        if os.path.exists(dbPath):
            os.remove(dbPath)
            print("Database file exists,deleting the file")
        else:
            os.mknod(dbPath)
        self.conn = sqlite3.connect(dbPath)
        print('Database is made in: {}'.format(dbPath))
        self.c = self.conn.cursor()
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
                            indexes_content TEXT NOT NULL,
                            PRIMARY KEY(word, documentName),
                            FOREIGN KEY (word) REFERENCES IndexWord(word)
                                ); 
                            CREATE TABLE Existing(doesExist BOOLEAN NOT NULL CHECK (doesExist IN (0,1)));''')
            self.conn.commit()
        except Exception as err:
            print("Database creation failed: {}".format(str(err)))

    def insertWord(self, lista):
        try:
            kurs = self.conn.cursor()
            for item in lista:
                kurs.execute("INSERT INTO IndexWord(word) VALUES(?)", [item])
            self.conn.commit()
        except Exception as err:
            print('Inserting into IndexWord table failed : {}'.format(str(err)))

    def insertPosting(self, postlist):
        try:
            kurs = self.conn.cursor()
            for item in postlist:
                kurs.execute\
                    ("INSERT INTO Posting(word,documentName,frequency,indexes,indexes_content) VALUES(?,?,?,?,?)", item)
            self.conn.commit()
        except Exception as err:
            print('Inserting into Posting table failed : {}'.format(str(err)))

        #exists("0","1")
    def insertExists(self, exists):
        kurs = self.conn.cursor()
        try:
            kurs.execute("INSERT INTO Existing(doesExist) VALUES (?)", exists)
            self.conn.commit()
        except Exception as err:
            print("Inserting into Existing table failed : {}".format(str(err)))

    def getExists(self):
        kurs = self.conn.cursor()
        try:
            kurs.execute("SELECT * FROM Existing")
            self.conn.commit()
            return True if int(self.c.fetchone()[0]) else False
        except Exception as err:
            print("Query failed {}".format(err))

    def getPostingsOfWord(self,listOfWords):
        query = f"SELECT * FROM Posting WHERE word in ({','.join(['?'] * len(listOfWords))})"
        kurs = self.conn.cursor()
        kurs.execute(query,listOfWords)
        rows = kurs.fetchall()
        return rows

