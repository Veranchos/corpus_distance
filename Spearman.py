from scipy.stats import spearmanr
from corpus import create_vectors


def compute_spearman (corpus1, corpus2):
    vector1 = [value for key,value in corpus1]
    vector2 = [value for key,value in corpus2]

    result = spearmanr(vector1, vector2)

    # print(result.correlation)

    return result.correlation


