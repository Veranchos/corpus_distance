from scipy.stats import chisquare
from corpus import relativization
from scipy.stats import chisquare, chi2_contingency
import numpy as np

def create_contingency_table(vector1, vector2, n):
    n_vector1 = vector1[:n]
    n_vector2 = vector2[:n]
    n_vector1.append(sum(vector1[n:]))
    n_vector2.append(sum(vector2[n:]))

    return np.array([relativization(n_vector1), relativization(n_vector2)])

def chi_square(corpus1, corpus2, interval):
    start, end = interval
    vector1 = [value for key, value in corpus1]
    vector2 = [value for key, value in corpus2]

    obs = create_contingency_table(vector1[start:], vector2[start:], end)

    chi2= sum(chisquare(obs).statistic)

    print(chi2)

    return chi2