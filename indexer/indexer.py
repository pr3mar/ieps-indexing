# -*- coding: utf-8 -*-
import argparse
from documentQuerying import DocumentQuerying
from preprocess import Preprocess
from utils import timing
from index import IndexFactory
from db import DB
from index import ReverseIndex

# executes the:
#   - pre-processing
#   - indexing
#   - querying
@timing
def main(indexType, inputPath, outputPath, userQuery, run=True):
    inputTokens = Preprocess.preprocessFiles(inputPath, outputPath)
    db = DB(inputPath)
    index = IndexFactory.getIndexByType(indexType, inputTokens, outputPath, db)
    rev = ReverseIndex(inputTokens, outputPath,db)
    rev.writeToDb()

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
    main('reverse', '../input', '../output', 'my query')
