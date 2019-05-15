import glob
import re
import json
import os
from utils import timing
from nltk.tokenize import word_tokenize
from inscriptis import get_text
from .stopwords import stop_words_slovene


class Preprocess:

    @staticmethod
    def tokenize(text):
        return [token for token in word_tokenize(text) if token not in stop_words_slovene]

    @staticmethod
    def contentize(text):
        return [token for token in word_tokenize(text)]

    @staticmethod
    @timing
    def preprocessFiles(rootInputPath, outputPath, forceUpdate=True):
        outputFilePath = f"{outputPath}/processed.json"
        if os.path.isfile(outputFilePath) and forceUpdate == False:
            with open(outputFilePath, "r") as file:
                return json.load(file)
        processed = []
        # Find all .html files
        inputPaths = [f for f in glob.glob(rootInputPath + "**/*.html", recursive=True)]
        for idx, documentPath in enumerate(inputPaths):
            print(f"[{(idx / len(inputPaths)) * 100:.0f}%] Working on {documentPath}")
            with open(documentPath, 'r') as file:
                text = re.sub(r'<[^<]+?>', '', get_text(file.read().lower()))
                content = Preprocess.contentize(text)
                tokens = Preprocess.tokenize(text)
                processed.append({
                    "fileName": re.compile(r'.*/(.*).html').search(documentPath).group(1),
                    "tokens": tokens,
                    "content": content
                })
        with open(outputFilePath, "w") as file:
            json.dump(processed, file, indent=4)
        return processed


# inputF = '/home/stefan/4th semester/Web Information Extraction And Retrieval/ieps-indexing/input'
# outputF = '/home/stefan/4th semester/Web Information Extraction And Retrieval/ieps-indexing/output'
# Preprocess.preprocessFiles(inputF, outputF)