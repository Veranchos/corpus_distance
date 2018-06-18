from scipy.stats import spearmanr
from corpus import create_vectors

import csv


def compute_spearman (corpus1, corpus2, interval):
    start, end = interval
    vector1 = [value for key,value in corpus1]
    vector2 = [value for key,value in corpus2]

    result = spearmanr(vector1[start:end], vector2[start:end])

    # print(result)

    return 1 - result.correlation


