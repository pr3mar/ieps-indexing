from preprocess import Preprocess


class Index(object):
    def __init__(self, inputPath, outputPath, forceRecreate=False):
        self.inputPath = inputPath
        self.outputPath = outputPath
        self.forceRecreate = forceRecreate
        self.preprocessed = Preprocess.preprocessFiles(self.inputPath, self.outputPath, self.forceRecreate)
        self.indexerType = "None"
        self.type = "None"

    def buildIndex(self):
        # Builds the index
        pass

    def search(self, query):
        # searches the index
        pass

