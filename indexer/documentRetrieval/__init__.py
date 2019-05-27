from utils import timing
from preprocess import Preprocess
import texttable as tt
import random


class DocumentRetrieval:
    def __init__(self, indexer):
        self.indexer = indexer

    def __printResults(self, resultSet, numResults = 10):
        preprocessed = self.indexer.preprocessed
        processed = 0
        table = tt.Texttable()
        table.header(["Rank", "Frequency", "Document", "Snippet"])
        table.set_cols_width([5, 10, 30, 100])
        table.set_cols_dtype(["i", "i", "t", "t"])
        for result in resultSet:
            if processed >= numResults:
                break
            documentName = result[0]
            frequency = result[1]
            indices = sorted([int(x) for x in result[2].split(",")])
            snippet = ""
            content = preprocessed[documentName]["content"]
            for i in range(min(5, len(indices))):
                idx = indices[i]
                snippet += " ".join(content[idx-3:idx])
                snippet += f" *{content[idx]}* "
                snippet += " ".join(content[idx + 1:idx + 4])
                snippet += " ... "
            table.add_row((processed + 1, frequency, documentName, snippet))
            processed += 1
        if processed > 0:
            print(table.draw())
        else:
            print("No results found.")

    def query(self, userQuery, numResults=15):
        timePassed, resultSet = self.indexer.search(Preprocess.tokenize(userQuery))
        print(f"[{self.indexer.indexerType}] Found {len(resultSet)} results in {timePassed:.2f} ms")
        self.__printResults(resultSet, numResults=numResults)
        return resultSet

    def randomTokens(self):
        preprocessed = self.indexer.preprocessed
        file = random.choice(list(preprocessed.keys()))
        return " ".join(random.sample(preprocessed[file]["tokens"], random.randint(2, 5)))

    def benchmark(self, repetitions=100):
        avgTime = 0.0
        queries = []
        for i in range(10):
            query = self.randomTokens()
            timepassed, resultSetPrev = self.indexer.search(Preprocess.tokenize(query))
            for j in range(repetitions - 1):
                avgTime += timepassed
                timepassed, resultSet = self.indexer.search(Preprocess.tokenize(query))
                if len(resultSetPrev) != len(resultSet):
                    raise Exception(f"Not equal result set??? Query: {query}")
                resultSetPrev = resultSet
            queries.append((query, len(resultSetPrev)))
            avgTime += timepassed
        return queries, avgTime/(10 * repetitions)
