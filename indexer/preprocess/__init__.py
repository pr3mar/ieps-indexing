import glob
import re
import json
import os
from utils import timing
from nltk.tokenize import word_tokenize
from inscriptis import get_text
from .stopwords import stop_words_slovene

specialChars = ['!', '"', '""', "#", '$', '%', '&', '\'', '\'\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '``', '{', '|', '}', '~' ]
    
class Preprocess:

    
    @staticmethod
    def tokenize(text):
        return [token for token in word_tokenize(text) if token not in stop_words_slovene and token not in specialChars]

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
        content = []
        tokens = []
        fileName = []
        # Find all .html files
        inputPaths = [f for f in glob.glob(rootInputPath + "**/*.html", recursive=True)]
        for idx, documentPath in enumerate(inputPaths):
            print(f"[{(idx / len(inputPaths)) * 100:.0f}%] Working on {documentPath}")
            with open(documentPath, 'r') as file:
                text = re.sub(r'<[^<]+?>', '', get_text(file.read().lower()))
                content.append(Preprocess.contentize(text))
                tokens.append(Preprocess.tokenize(text))
                fileName.append(re.compile(r'.*/(.*).html').search(documentPath).group(1))
            
        processed = {
            filer: 
            {
                "tokens": tokens[i],
                "content": content[i]
            }for i, filer in enumerate(fileName)
        }
        
        with open(outputFilePath, "w") as file:
            json.dump(processed, file, indent=4)
        return processed