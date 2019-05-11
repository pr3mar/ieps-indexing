# -*- coding: utf-8 -*-
import re, glob, os
from bs4 import BeautifulSoup

# Create dir if it does not exist
dir = '../../output/preprocessed/'
if not os.path.exists(dir):
    os.makedirs(dir)

# Find all .html files
files = [f for f in glob.glob('../../input/' + "**/*.html", recursive=True)]

# Pre-processing
for fileLoc in files:
    # Files reading
    file = open(fileLoc, 'r').read().lower().replace('\n', ' ')
    soup = BeautifulSoup(file, "lxml")
    [s.extract() for s in soup(['iframe', 'script', 'head'])]
    name = r'.*/(.*).html'
    matchName = re.compile(name).search(fileLoc)
    name = dir + matchName.group(1)
    file = open(name + '.txt', 'w')
    file.write(soup.text)
    file.close()