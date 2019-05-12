from .ReverseIndex import ReverseIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getIndexByType(indexType, inputPath, outputPath, db):
        if indexType == "reverse":
            return ReverseIndex(inputPath, outputPath, db)
        elif indexType == "sequential":
            return SequantialIndex(inputPath, outputPath, db)
        else:
            raise Exception("Unknown index type")
