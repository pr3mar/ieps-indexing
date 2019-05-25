from utils import timing
from preprocess import Preprocess
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputPath, outputPath, forceRecreate):
        super(SequantialIndex, self).__init__(inputPath, outputPath, forceRecreate)
        self.preprocessed = {}

    @timing
    def buildIndex(self):
        self.preprocessed = Preprocess.preprocessFiles(self.inputPath, self.outputPath, self.forceRecreate)

    @timing
    def search(self, query):
        results = []
        for documentName in self.preprocessed:
            indices = [str(i) for i, x in enumerate(self.preprocessed[documentName]["content"]) if x in query]
            if len(indices) > 0:
                results.append((documentName, len(indices), ",".join(indices)))
        results.sort(key=lambda x: x[1], reverse=True)
        return results
