from csvReader import read_csv
from corpus import create_vectors, normalize_corpora
from vectors import compare_sub_vectors_distance, compare_vectors_distance, calculate_distance_between_vectors_in_interval
from kilgarriff import create_known_similarity_corpora, compare_known_similarity_corpora


corpus1 = read_csv('written_medium_book.csv')
corpus2 = read_csv('wl_2018-03-14_23_23_58.csv')

c1, c2 = normalize_corpora(corpus1, corpus2)

print(c1, c2)
#
# vector1, vector2 = create_vectors(corpus1, corpus2)
# sub_vector_distance = compare_sub_vectors_distance(vector1, vector2, 100, 10)
#
# print(sub_vector_distance)
# print('full vector - ', compare_vectors_distance(vector1, vector2))

corpora = create_known_similarity_corpora(c1, c2)


def func(corpus1, corpus2):
    vector1, vector2 = create_vectors(corpus1, corpus2)
    # distance = compare_vectors_distance(vector1, vector2)
    interval = len(vector1) // 10
    distance = calculate_distance_between_vectors_in_interval(vector1, vector2, [100, len(vector1)])
    return distance


result = compare_known_similarity_corpora(corpora, func)

print(result)

# for row in corpora:
#     print(row)