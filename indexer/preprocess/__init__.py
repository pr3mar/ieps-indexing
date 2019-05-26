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
        return list(set([token for token in word_tokenize(text.lower()) if token not in stop_words_slovene and re.match('\w', token)]))

    @staticmethod
    def contentize(text):
        return [token for token in word_tokenize(text)]

    @staticmethod
    @timing
    def preprocessFiles(rootInputPath, outputPath, forceRecreate=False, debugInfo=False):
        outputFilePath = f"{outputPath}/processed.json"
        if os.path.isfile(outputFilePath) and not forceRecreate:
            with open(outputFilePath, "r") as file:
                return json.load(file)
        print("Preprocessing...")
        processed = {}
        inputPaths = [f for f in glob.glob(rootInputPath + "**/*.html", recursive=True)]
        for idx, documentPath in enumerate(inputPaths):
            if debugInfo: print(f"[{(idx / len(inputPaths)) * 100:.0f}%] Working on {documentPath}")
            with open(documentPath, mode='r', encoding="utf-8") as file:
                text = re.sub(r'<[^<]+?>', '', get_text(file.read().lower()))
                processed[re.compile(r'.*/(.*).html').search(documentPath).group(1)] = {
                    "tokens": Preprocess.tokenize(text),
                    "content": Preprocess.contentize(text)
                }
        with open(outputFilePath, mode="w", encoding="utf-8") as file:
            json.dump(processed, file, ensure_ascii=False)
        return processed
