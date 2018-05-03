# coding: utf-8
from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer

import csv

# bnc_reader = BNCCorpusReader(root='./2554/2554/download/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')
bnc_reader = BNCCorpusReader(root='./2554/2554/download/Texts/', fileids=r'A/A1/\w*\.xml')
tokenizer = RegexpTokenizer(r'\w+')


words = [word.lower() for word in bnc_reader.words()]

tokens = tokenizer.tokenize(" ".join(words))
# tokens = [token.encode('utf-8') for token in tokens]

fdist1 = FreqDist(tokens).items()


sorted_fdist = sorted(fdist1, key=lambda item: item[1], reverse=True)

csvfile = "./exported/A1.csv"

with open(csvfile, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(sorted_fdist)