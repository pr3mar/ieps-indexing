from utils import timing
from nltk.corpus import stopwords


class Preprocess:

    def tokenize(self, input):
        tokens = word_tokenize(text)
        tokens = [i for i in tokens if i not in stop_words_slovene]
        return tokens

    @staticmethod
    @timing
    def preprocess(inputPath, outputPath, dumpToFile=False):
        # TODO: @Stefan copy the code here
        # return in the following format
        # [
        #     {
        #         "fileName": "<inputFileName>", // just the name, not the entire path
        #         "tokens": ["<token1>", "<token2>"]
        #     },
        #     {
        #         "fileName": "<inputFileName>",
        #         "tokens": ["<token1>", "<token2>"]
        #     },
        #     ...
        #     {
        #         "fileName": "<inputFileName>",
        #         "tokens": ["<token1>", "<token2>"]
        #     },
        # ]
        return []
