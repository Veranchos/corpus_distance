from scipy.spatial import distance

def manhattan(corpus1, corpus2):
    vector1 = [value for key, value in corpus1]
    vector2 = [value for key, value in corpus2]
    dist = distance.cityblock(vector1, vector2)
    return dist