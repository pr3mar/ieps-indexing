from utils import timing, timed
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputPath, outputPath, forceRecreate):
        super(SequantialIndex, self).__init__(inputPath, outputPath, forceRecreate)
        self.indexerType = "Sequential Index"
        self.type = "sequential"

    @timed
    def buildIndex(self):
        pass

    @timed
    def search(self, query):
        results = []
        for documentName in self.preprocessed:
            indices = [str(i) for i, x in enumerate(self.preprocessed[documentName]["content"]) if x in query]
            if len(indices) > 0:
                results.append((documentName, len(indices), ",".join(indices)))
        results.sort(key=lambda x: x[1], reverse=True)
        return results
