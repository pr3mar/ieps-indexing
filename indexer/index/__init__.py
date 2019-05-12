from .ReverseIndex import ReverseIndex
from .SequentialIndex import SequantialIndex


class IndexFactory:
    @staticmethod
    def getReverseIndex():
        return ReverseIndex()

    @staticmethod
    def getSequentialIndex():
        return SequantialIndex()
