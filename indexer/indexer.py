from documentQuerying import DocumentQuerying
from preprocess import Preprocess
from utils import timing
from index import IndexFactory


# executes the:
#   - pre-processing
#   - indexing
#   - querying
@timing
def main(inputPath, outputPath, userQuery, run=True):
    Preprocess.preprocess(inputPath, outputPath)
    reverseIndex = IndexFactory.getReverseIndex()
    seqIndex = IndexFactory.getSequentialIndex()
    reverseIndex.buildIndex()
    seqIndex.buildIndex()
    query = DocumentQuerying(userQuery, reverseIndex)


# get user arguments:
#   - input and output paths,
#   - operation mode [build, run]
#       - build -> builds the indices
#       - run   -> executes a query on the built indices
#   - [optional] indexer kind [inverse, sequential] -> if we are not running the query we do not need this
#   - [optional] user query -> if an index is being built we do not need this
def processArgs():
    pass


if __name__ == "__main__":

    main('input', 'output', 'my query')
