from scipy.stats import chisquare
from corpus import relativization
from scipy.stats import chisquare
import numpy as np

def create_contingency_table(vector1, vector2, n):
    n_vector1 = vector1[:n]
    n_vector2 = vector2[:n]
    n_vector1.append(sum(vector1[n:]))
    n_vector2.append(sum(vector2[n:]))

    return np.array([relativization(n_vector1), relativization(n_vector2)]).T

def chi_square(vector1, vector2):
    obs = create_contingency_table(vector1, vector2, 2)
    result = chisquare(obs)
    return(result)
