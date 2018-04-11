PARTS = 10


def create_known_similarity_corpora(corpus1, corpus2):
    known_similarity_corpora = []
    for i in range(PARTS + 1):
        delimiter = i*len(corpus2)//PARTS
        sub_corpus = corpus1[:delimiter] + corpus2[delimiter:]
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

                    if distance2 < distance1:
                        right_counter += 1
                    counter += 1
    return counter / right_counter

    # return percent of right signs
