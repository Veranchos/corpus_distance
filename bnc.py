# coding: utf-8
from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer

import csv

# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'A\/(A1\/A1[D-Z]|A2\/\w*|A3\/\w*|A4\/\w*|A5\/A5[0-9A-X]).xml') W_newsp_brndsht
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'C\/CB\/CB[U-Y].xml') W_commerce
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'C\/(CN\/CN[A-Z]|CP\/\w*|CR\/CR[0-5]).xml') # W_app_science
tokenizer = RegexpTokenizer(r'\w+')


words = [word.lower() for word in bnc_reader.words()]

tokens = tokenizer.tokenize(" ".join(words))
# tokens = [token.encode('utf-8') for token in tokens]

fdist1 = FreqDist(tokens).items()


sorted_fdist = sorted(fdist1, key=lambda item: item[1], reverse=True)

csvfile = "./exported/W_app_science.csv"

with open(csvfile, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(sorted_fdist)