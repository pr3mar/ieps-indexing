# -*- coding: utf-8 -*-
import argparse
from documentQuerying import DocumentQuerying
from preprocess import Preprocess
from utils import timing
from index import IndexFactory
from db import DB

# executes the:
#   - pre-processing
#   - indexing
#   - querying
@timing
def main(indexType, inputPath, outputPath, userQuery, forceRecreate=False, run=True):
    index = IndexFactory.getIndexByType(indexType, inputPath, outputPath, forceRecreate)
    index.buildIndex()
    red = index.search(Preprocess.tokenize(userQuery))
    print(len(red))
    print(sum([x[1] for x in red]))
    query = DocumentQuerying(userQuery, index)



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
    main('inverse', '../input', '../output', 'Sistem SPOT')
    main('sequential', '../input', '../output', 'Sistem SPOT')
