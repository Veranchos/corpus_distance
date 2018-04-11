from readers.txt_reader import read_txt
from corpus import normalize_corpora, create_vectors
from vectors import compare_vectors_distance, calculate_distance_between_vectors_in_interval
from kilgarriff import compare_measurement

hp_corpus = read_txt('texts/HP.txt')
lotr_corpus = read_txt('texts/LOTR.txt')

normalized_hp_corpus, normalized_lotr_corpus = normalize_corpora(hp_corpus, lotr_corpus)

hp_vector, lotr_vector = create_vectors(hp_corpus, lotr_corpus)

full_distance = compare_vectors_distance(hp_vector, lotr_vector)

print('Full cosine distance between hp and lotr:', full_distance)

def func(corpus1, corpus2):
    vector1 = [value for key,value in corpus1]
    vector2 = [value for key,value in corpus2]
    return calculate_distance_between_vectors_in_interval(vector1, vector2, [50, len(vector1) // 2 + 50])

print(
    'Kilgarriff percent for cosine distance in interval [50,', len(normalized_lotr_corpus) // 2 + 50, ']:',
    compare_measurement(normalized_hp_corpus, normalized_lotr_corpus, func)
)