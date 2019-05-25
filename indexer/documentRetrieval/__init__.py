from utils import timing
from preprocess import Preprocess


class DocumentRetrieval:
    def __init__(self, indexer):
        self.indexer = indexer

    def transformOutput(self, resultSet):
        preprocessed = self.indexer.preprocessed
        processed = 0
        output = []
        for result in resultSet:
            if processed > 10:
                break
            documentName = result[0]
            frequency = result[1]
            indices = sorted([int(x) for x in result[2].split(",")])
            snippet = ""
            content = preprocessed[documentName]["content"]
            for i in range(5):
                idx = indices[i]
                snippet += " ".join(content[idx-3:idx])
                snippet += f" *{content[idx]}* "
                snippet += " ".join(content[idx + 1:idx + 4])
                snippet += " ... "
            output.append((frequency, documentName, snippet))
            processed += 1
        return output
    def query(self, userQuery):
        timePassed, resultSet = self.indexer.search(Preprocess.tokenize(userQuery))
        print(f"[{self.indexer.indexerType}] Results found for  in {timePassed:.2f} ms")
        print(self.transformOutput(resultSet))
