from random import shuffle
PARTS = 10


def randomize_words(corpus1, corpus2):
    random_corpus1 = []
    random_corpus2 = []
    corpora = []

    for i in range(len(corpus1)):
        corpora.append([corpus1[i], corpus2[i]])

    shuffle(corpora)

    for i in range(len(corpora)):
        item1, item2 = corpora[i]

        random_corpus1.append(item1)
        random_corpus2.append(item2)

    return [random_corpus1, random_corpus2]


def create_known_similarity_corpora(random_corpus1, random_corpus2):
    known_similarity_corpora = []
    for i in range(PARTS + 1):
        delimiter = i*len(random_corpus2)//PARTS
        sub_corpus = random_corpus1[:delimiter] + random_corpus2[delimiter:]
        known_similarity_corpora.append(sub_corpus)

    return known_similarity_corpora  # 11 corpora, including corpus1 and corpus2


def compare_known_similarity_corpora(ks_corpora, compare_corpora):
    corpora_length = len(ks_corpora)
    counter = 0
    right_counter = 0

    for c in range(corpora_length):
        for d in range(corpora_length-1, c+1, -1):
            for a in range(c, d + 1):
                for b in range(d, a, -1):
                    if c == a and b == d:
                        continue

                    distance1 = compare_corpora(ks_corpora[c], ks_corpora[d])
                    distance2 = compare_corpora(ks_corpora[a], ks_corpora[b])

                    print(distance1, distance2)

                    if distance2 < distance1:
                        right_counter += 1
                    counter += 1
    return right_counter / counter


def compare_measurement(corpus1, corpus2, compare_corpora):
    c1, c2 = randomize_words(corpus1, corpus2)
    ks_corpora = create_known_similarity_corpora(c1, c2)

    return compare_known_similarity_corpora(ks_corpora, compare_corpora)


    # return percent of right signs
