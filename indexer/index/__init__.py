from .ReverseIndex import ReverseIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getIndexByType(indexType, inputPath, outputPath, forceRecreate):
        if indexType == "reverse":
            return ReverseIndex(inputPath, outputPath, forceRecreate)
        elif indexType == "sequential":
            return SequantialIndex(inputPath, outputPath, forceRecreate)
        else:
            raise Exception("Unknown index type")
