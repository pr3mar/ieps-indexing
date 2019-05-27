# -*- coding: utf-8 -*-
import argparse
import os
from prompt_toolkit import PromptSession
from documentRetrieval import DocumentRetrieval
from utils import timing
from index import IndexFactory

# executes the:
#   - pre-processing
#   - indexing
#   - querying
@timing
def initIndexer(indexType, inputPath, outputPath, forceRecreate=False):
    index = IndexFactory.getIndexByType(indexType, inputPath, outputPath, forceRecreate)
    timePassed, result = index.buildIndex()
    print(f"[{index.indexerType}] Time required to build the index: {timePassed:.2f} ms")
    return DocumentRetrieval(index)


def search():
    pass


def repl(dr, numResults=10):
    session = PromptSession()
    helpMenu = """You have entered in the interactive mode, a list of supported commands: 
    - help this menu 
    - max-results <number> - sets the maximum number of results obtained, 
    - recreate - recreates the current indexer method
    - indexer-type (inverted|sequential) - sets the type of the indexer
    - exit - exits the REPL mode
    - anything else performs a search on the chosen index
"""
    print(helpMenu)
    while True:
        try:
            text = session.prompt(f"[{dr.indexer.indexerType}]> Enter query: ")
        except KeyboardInterrupt:
            print("Exit by pressing ctrl+D")
            continue
        except EOFError:
            break
        else:
            if text.startswith("max-results"):
                try:
                    numResults = int(text.split(" ")[1])
                except Exception:
                    print("Try again: `max-results <number>`")
            elif text.startswith("indexer-type"):
                try:
                    dr = initIndexer(text.split(" ")[1], dr.indexer.inputPath, dr.indexer.outputPath, forceRecreate=False)
                except Exception:
                    print("Try again: `indexer-type (inverted|sequential)`")
            elif text == "recreate":
                try:
                    dr = initIndexer(dr.indexer.type, dr.indexer.inputPath, dr.indexer.outputPath, forceRecreate=True)
                except Exception:
                    print("Try again: `indexer-type (inverted|sequential)`")
            elif text == "exit":
                break
            elif text == "help":
                print(helpMenu)
            else:
                print('Your query:', text)
                dr.query(text, numResults=numResults)
    print('exiting')


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The path `{arg}` does not exist!")
    else:
        return arg

# get user arguments:
#   - input and output paths,
#   - operation mode [build, run]
#       - build -> builds the indices
#       - run   -> executes a query on the built indices
#   - [optional] indexer kind [inverse, sequential] -> if we are not running the query we do not need this
#   - [optional] user query -> if an index is being built we do not need this
def processArgs():
    parser = argparse.ArgumentParser(description='Inverted index builder and retriever by Marko Prelevikj, Gojko Hajdukovic and Stefan Ivanisevic')
    parser.add_argument('-i', '--input', required=True, default='empty',
                        help='[required] Input file', metavar="FILE",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-o', '--output', required=True, default='empty',
                        help='[required] Output file', metavar="FILE")
    parser.add_argument('-m', '--method', required=False, default='inverted',
                        help='[optional] Which method to use to build/retrieve the index. Available options: (inverted|sequential), default is inverted.')
    parser.add_argument('--force-recreate', required=False, default=None, action='store_true',
                        help='[optional] Forces the indices to be recreated.')
    parser.add_argument('--interactive', required=False, default=False, action='store_true',
                        help='[optional] Enables interactive mode where the user can enter multiple queries.')
    parser.add_argument('--benchmark', required=False, default=None, type=int,
                        help='[optional] Benchmarks the performance N times against a random query')
    parser.add_argument('--query', required=False, default=None,
                        help='[optional] Query to be executed (enter it in quotation marks)')
    parser.add_argument('--num-results', required=False, default=10, type=int,
                        help='[optional] Sets the number of retrieved results (default = 10)')
    return parser.parse_args()


if __name__ == "__main__":
    args = processArgs()
    dr = initIndexer(args.method, args.input, args.output, forceRecreate=args.force_recreate)
    if args.interactive:
        repl(dr, args.num_results)
    elif args.query:
        dr.query(args.query, numResults=args.num_results)
    elif args.benchmark:
        if args.benchmark > 1000:
            print("Maximum number of repetitions is 1000.")
            args.benchmark = 1000
        if args.benchmark < 25:
            print("Minimum number of repetitions is 25.")
            args.benchmark = 25
        queries, result = dr.benchmark(args.benchmark)
        print(f"Average time needed for {args.benchmark} the following queries:")
        for query in queries:
            print(f"\t- `{query[0]}`, #results: {query[1]}")
        print(f"with {dr.indexer.indexerType} was {result} ms.")
