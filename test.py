from csvReader import read_csv
from corpus import create_vectors, normalize_corpora
from vectors import compare_sub_vectors_distance, compare_vectors_distance, calculate_distance_between_vectors_in_interval, compare_vectors_distance_2, manhattan_distance
from kilgarriff import create_known_similarity_corpora, compare_known_similarity_corpora


# corpus1 = read_csv('written_medium_book.csv')
# corpus2 = read_csv('wl_2018-03-14_23_23_58.csv')
corpus3 = read_csv('written_academic_medicine.csv')
corpus4 = read_csv('written_fiction_poetry.csv')

c3, c4 = normalize_corpora(corpus3, corpus4)

print(c3, c4)

vector3, vector4 = create_vectors(corpus3, corpus4)
# sub_vector_distance = compare_sub_vectors_distance(vector1, vector2, 100, 10)
#
# print(sub_vector_distance)
# print('full vector - ', compare_vectors_distance(vector1, vector2))
#
# corpora = create_known_similarity_corpora(c1, c2)
#
#
# def func(corpus1, corpus2):
#     vector1, vector2 = create_vectors(corpus1, corpus2)
#     # distance = compare_vectors_distance(vector1, vector2)
#     interval = len(vector1) // 10
#     distance = calculate_distance_between_vectors_in_interval(vector1, vector2, [100, len(vector1)])
#     return distance
#
#
# result = compare_known_similarity_corpora(corpora, func)
#
# print(result)

# for row in corpora:
#     print(row)

print(compare_vectors_distance_2(vector3, vector4))
print(compare_vectors_distance_2(vector3, vector3))
print(compare_vectors_distance(vector3, vector4))

scipy.stats.chisquare(f_obs, f_exp=None, ddof=0, axis=0)