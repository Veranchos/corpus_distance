from readers.txt_reader import read_txt
from corpus import normalize_corpora, calculate_N

hp_corpus = read_txt('texts/HP.txt')
lotr_corpus = read_txt('texts/LOTR.txt')

normalized_hp_corpus, normalized_lotr_corpus = normalize_corpora(hp_corpus, lotr_corpus)

# print(c5)
# print(c6)
#
# vector3, vector4 = create_vectors(c3, c4)
# # sub_vector_distance = compare_sub_vectors_distance(vector1, vector2, 100, 10)
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
#
# print(compare_vectors_distance_2(vector3, vector4))
# print(compare_vectors_distance_2(vector3, vector3))
# print(compare_vectors_distance(vector3, vector4))
#
# vector = [(vector3[index] + vector4[index]) / 2 for index in range(len(vector4))]
# new_vector = [[vector3[index], vector4[index]] for index in range(len(vector4))]