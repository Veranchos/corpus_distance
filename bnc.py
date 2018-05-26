# coding: utf-8
from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer

import csv

def create_wordlist_from_subcorpus(name, regexp):
    bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=regexp)

    words = [word.lower() for word in bnc_reader.words()]

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(" ".join(words))

    fdist1 = FreqDist(tokens).items()

    sorted_fdist = sorted(fdist1, key=lambda item: item[1], reverse=True)

    csvfile = f'./exported/${name}.csv'

    with open(csvfile, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(sorted_fdist)


def read_bnc_subcorpus(name, regexp):
    bnc_reader = BNCCorpusReader(root='./BNC/texts/', fileids=regexp)

    words = [word.lower() for word in bnc_reader.words()]
    tokenizer = RegexpTokenizer(r'\w+')

    tokens = tokenizer.tokenize(" ".join(words))

    csvfile = f'./words/{name}.csv'
    with open(csvfile, "w", encoding='utf-8') as output:
        writer = csv.writer(output, lineterminator='\n')
        for row in tokens:
            writer.writerow([row])

# read_bnc_subcorpus('ACC', r'C\/CB\/CB[T-Y].xml') # Accountancy (ACC)
# read_bnc_subcorpus('GUA', r'A\/A([89]\/\w*|7\/A7[S-Y]|A\/AA[0-9A-Y]).xml') # The Guardian (GUA)
# read_bnc_subcorpus('ART', r'(E\/EB\/EB[S-X]|C\/CK\/CK[T-Y]).xml') # The Art Newspaper (ART)
# read_bnc_subcorpus('BMJ', r'F\/F(S\/FSY|T\/FT[0-5]).xml') # British Medical Journal (BMJ)
# read_bnc_subcorpus('TOD', r'C\/C(B\/CB[C-G]|E\/CE[K-P]).xml') # Today (TOD)
# read_bnc_subcorpus('SCO', r'K\/K5\/K5[6-9A-M].xml') # The Scotsman (SCO)
# read_bnc_subcorpus('ENV', r'J\/J(2\/J2[N-Y]|3\/J3[0-9A-L]).xml') # Environment Digest (ENV)

# create_wordlist_from_subcorpus('ACC', r'C\/CB\/CB[T-Y].xml') # Accountancy (ACC)
# create_wordlist_from_subcorpus('GUA', r'A\/A([89]\/\w*|7\/A7[S-Y]|A\/AA[0-9A-Y]).xml') # The Guardian (GUA)
# create_wordlist_from_subcorpus('ART', r'(E\/EB\/EB[S-X]|C\/CK\/CK[T-Y]).xml') # The Art Newspaper (ART)
# create_wordlist_from_subcorpus('BMJ', r'F\/F(S\/FSY|T\/FT[0-5]).xml') # British Medical Journal (BMJ)
# create_wordlist_from_subcorpus('TOD', r'C\/C(B\/CB[C-G]|E\/CE[K-P]).xml') # Today (TOD)
# create_wordlist_from_subcorpus('SCO', r'K\/K5\/K5[6-9A-M].xml') # The Scotsman (SCO)
# create_wordlist_from_subcorpus('ENV', r'J\/J(2\/J2[N-Y]|3\/J3[0-9A-L]).xml') # Environment Digest (ENV)
