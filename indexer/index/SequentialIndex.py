import json
from utils import timing
from preprocess import Preprocess
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputPath, outputPath, forceRecreate):
        super(SequantialIndex, self).__init__(inputPath, outputPath, forceRecreate)
        self.inputTokens = Preprocess.preprocessFiles(self.inputPath, self.outputPath, self.forceRecreate)

    @timing
    def buildIndex(self):
        pass  # we do not need to build anything here, as we already have the preprocessed text

    @timing
    def search(self, query):
        results = []
        for documentName in self.inputTokens:
            indices = [str(i) for i, x in enumerate(self.inputTokens[documentName]["content"]) if x in query]
            if len(indices) > 0:
                results.append((documentName, len(indices), ",".join(indices)))
        results.sort(key=lambda x: x[1], reverse=True)
        return results
