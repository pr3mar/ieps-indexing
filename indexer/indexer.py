# -*- coding: utf-8 -*-
import argparse
from documentRetrieval import DocumentRetrieval
from utils import timing
from index import IndexFactory

# executes the:
#   - pre-processing
#   - indexing
#   - querying
@timing
def main(indexType, inputPath, outputPath, userQuery, forceRecreate=False):
    index = IndexFactory.getIndexByType(indexType, inputPath, outputPath, forceRecreate)
    timePassed, result = index.buildIndex()
    print(f"[{index.indexerType}] Time required to build the index: {timePassed:.2f} ms")
    dr = DocumentRetrieval(index)
    dr.query(userQuery)



# get user arguments:
#   - input and output paths,
#   - operation mode [build, run]
#       - build -> builds the indices
#       - run   -> executes a query on the built indices
#   - [optional] indexer kind [inverse, sequential] -> if we are not running the query we do not need this
#   - [optional] user query -> if an index is being built we do not need this
def processArgs():
    parser = argparse.ArgumentParser()
    parser.parse_args()


if __name__ == "__main__":
    main('inverted', '../input', '../output', 'Republika Slovenija')
    main('sequential', '../input', '../output', 'Republika Slovenija')
