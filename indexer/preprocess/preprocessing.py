# -*- coding: utf-8 -*-
import re
import glob
import time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from stopwords import stop_words_slovene

class PreprocessingText:
    def prep(inputPath, outputPath):

        def tokenize(text):
            tokens = word_tokenize(text)
            tokens = [i for i in tokens if i not in stop_words_slovene]
            return tokens
            
        def writeData(name, text):
            file = open(outputPath + name, 'w')
            file.write(text)
            file.close()


        # Find all .html files
        files = [f for f in glob.glob(inputPath + "**/*.html", recursive=True)]
        for fileLoc in files:
            # Files reading
            file = open(fileLoc, 'r').read().lower().replace('\n', ' ')
            soup = BeautifulSoup(file, "lxml")
            [s.extract() for s in soup(['iframe', 'script', 'head'])]
            tokens = tokenize(str(soup.text))
            name = r'.*/(.*).html'
            matchName = re.compile(name).search(fileLoc)
            name = matchName.group(1) + '.txt'
            writeData(name, str(tokens))
