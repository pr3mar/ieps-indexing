import json
from utils import timing
from preprocess import Preprocess
from .index import Index


class SequantialIndex(Index):
    def __init__(self, inputPath, outputPath, forceRecreate):
        super(SequantialIndex, self).__init__(inputPath, outputPath, db, forceRecreate)

    @timing
    def buildIndex(self):
        pass  # we do not need to build anything here, as we already have the preprocessed text

    @timing
    def search(self, query):
        results = {}
        # print(f"query: {Preprocess.tokenize(userQuery)}")
        for queryToken in Preprocess.tokenize(userQuery):
            results[queryToken] = {
                "allResults": 0,
                "results": []
            }
            for document in self.inputTokens:
                indices = [i for i, x in enumerate(document["tokens"]) if x == queryToken]
                if len(indices) > 0:
                    results[queryToken]["allResults"] += len(indices)
                    results[queryToken]["results"].append({
                        "documentName": document["fileName"],
                        "resultIndices": indices
                    })
            results[queryToken]["results"].sort(key=lambda x: len(x["resultIndices"]), reverse=True)
        return results
