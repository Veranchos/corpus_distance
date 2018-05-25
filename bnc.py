# coding: utf-8
from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer

import csv

# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'C\/CB\/CB[T-Y].xml') # Accountancy (ACC)
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'A\/A([89]\/\w*|7\/A7[S-Y]|A\/AA[0-9A-Y]).xml') # The Guardian (GUA)
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'(E\/EB\/EB[S-X]|C\/CK\/CK[T-Y]).xml') # The Art Newspaper (ART)
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'F\/F(S\/FSY|T\/FT[0-5]).xml') # British Medical Journal (BMJ)
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'C\/C(B\/CB[C-G]|E\/CE[K-P]).xml') # Today (TOD)
# bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'K\/K5\/K5[6-9A-M].xml') # The Scotsman (SCO)
bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=r'J\/J(2\/J2[N-Y]|3\/J3[0-9A-L]).xml') # Environment Digest (ENV)
tokenizer = RegexpTokenizer(r'\w+')


words = [word.lower() for word in bnc_reader.words()]

tokens = tokenizer.tokenize(" ".join(words))
# tokens = [token.encode('utf-8') for token in tokens]

fdist1 = FreqDist(tokens).items()


sorted_fdist = sorted(fdist1, key=lambda item: item[1], reverse=True)

csvfile = "./exported/ENV.csv"

with open(csvfile, "w", encoding='utf-8') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(sorted_fdist)