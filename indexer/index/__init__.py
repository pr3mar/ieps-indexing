from .InverseIndex import InverseIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getIndexByType(indexType, inputPath, outputPath, forceRecreate):
        if indexType == "inverse":
            return InverseIndex(inputPath, outputPath, forceRecreate)
        elif indexType == "sequential":
            return SequantialIndex(inputPath, outputPath, forceRecreate)
        else:
            raise Exception("Unknown index type")
