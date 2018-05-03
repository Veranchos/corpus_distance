from readers.txt_reader import read_txt
from readers.csv_reader import read_csv
from Spearman import compute_spearman
from corpus import normalize_corpora, create_vectors
from vectors import compare_vectors_distance, calculate_distance_between_vectors_in_interval, compare_sub_vectors_distance
from kilgarriff import compare_measurement, ksc_in_intervals, find_best_interval


wmb = read_csv('exported/A0.csv')
wl = read_csv('exported/A1.csv')

hp_corpus = read_txt('texts/HP.txt')
lotr_corpus = read_txt('texts/LOTR.txt')

normalized_hp_corpus, normalized_lotr_corpus = normalize_corpora(hp_corpus, lotr_corpus)
normalized_wmb, normalized_wl = normalize_corpora(wmb, wl)


def func2(corpus1, corpus2):
    vector1 = [value for key,value in corpus1]
    vector2 = [value for key,value in corpus2]

    return compare_vectors_distance(vector1, vector2,)

# print(compute_spearman(wmb[100:], wl[100:]))

#

print(len(normalized_wl))

best_spearman_interval = find_best_interval(normalized_wmb, normalized_wl, compute_spearman)
print('------')
print(best_spearman_interval)
print(compare_measurement(normalized_wmb, normalized_wl, compute_spearman))
print(ksc_in_intervals(normalized_wmb, normalized_wl, compute_spearman, best_spearman_interval, 10))
# print(compare_vectors_distance_between_corpora(wmb[:100], wl[:100]))


# print(
#     'Kilgarriff percent for cosine distance in interval [50,', len(normalized_lotr_corpus) // 2 + 50, ']:',
#     compare_measurement(normalized_hp_corpus, normalized_lotr_corpus, func([8480, 24056]))
# )
#

# print(ksc_in_intervals(normalized_hp_corpus, normalized_lotr_corpus, func, 10, 10))

