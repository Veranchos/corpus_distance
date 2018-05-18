from scipy.spatial import distance
from corpus import create_vectors

def euclidean(corpus1, corpus2):
    vector1 = [value for key, value in corpus1]
    vector2 = [value for key, value in corpus2]
    dist = distance.euclidean(vector1, vector2)

    return dist