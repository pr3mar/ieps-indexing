from utils import timing
import glob
from nltk.corpus import stopwords
import nltk
import os


class Preprocess:

    def tokenize(self, input):
        tokens = nltk.word_tokenize(text)
        tokens = [i for i in tokens if i not in stopwords.stop_words_slovene]
        return tokens

    @staticmethod
    @timing
    def preprocess(inputPath, outputPath, dumpToFile=False):
        # TODO: @Stefan copy the code here
        # return in the following format
        #files = [i for i in glob.glob(inputPath + '**/*.html',recursive=True)]
        # for root, subFolders, files in os.walk(inputPath):
        #    for folder in subFolders:
        #        folderOut = open(outputPath, 'w')
        #        for file in files:
        #            filePath = os.path.join(root, file)
        #            toWrite = open(filePath).lower().read()
        #            print
        #            "Writing '" + toWrite + "' to" + filePath
        #            folderOut.write(toWrite)
        #        folderOut.close()



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

