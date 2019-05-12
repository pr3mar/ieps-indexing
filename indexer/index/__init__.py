from .ReverseIndex import ReverseIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getIndexByType(indexType, inputPath, outputPath):
        if indexType == "reverse":
            return ReverseIndex(inputPath, outputPath)
        elif indexType == "sequential":
            return SequantialIndex(inputPath, outputPath)
        else:
            raise Exception("Unknown index type")
