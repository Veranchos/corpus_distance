def get_words(corpus):
    return [row[0] for row in corpus]

def ipm(corpus):
    words_counter = 0
    for row in corpus:
        occurrence = row[1]
        words_counter += occurrence

    factor = (words_counter / 1000000)
    corpus_ipm = [[word, occurrence / factor] for word, occurrence in corpus]

    return corpus_ipm

def normalize_corpora(corpus1, corpus2):
    corpus_ipm1 = ipm(corpus1)
    corpus_ipm2 = ipm(corpus2)

    return union_words(corpus_ipm1, corpus_ipm2)


def get_sorted_union_corpora(corpus1, corpus2):
    words1 = get_words(corpus1)
    words2 = get_words(corpus2)
    all_words = set.union(set(words1), set(words2))

    dict1 = dict(corpus1)
    dict2 = dict(corpus2)

    word_occurrences = {}

    for word in all_words:
        occurrence1 = 0
        occurrence2 = 0

        if word in dict1:
            occurrence1 = dict1[word]
        if word in dict2:
            occurrence2 = dict2[word]

        word_occurrences[word] = [occurrence1, occurrence2]

    sorted_corpora = sorted(word_occurrences.items(), key=lambda row: sum(row[1]), reverse=True)

    return sorted_corpora # [ [word, [occurrence1, occurrence2]], ... ]


def union_words(corpus1, corpus2):
    corpora = get_sorted_union_corpora(corpus1, corpus2)

    new_corpus1 = []
    new_corpus2 = []

    for word, occurrences in corpora:
        new_corpus1.append([word, occurrences[0]])
        new_corpus2.append([word, occurrences[1]])

    return [new_corpus1, new_corpus2]


def create_vectors(corpus1, corpus2):
        corpora = get_sorted_union_corpora(corpus1, corpus2)

        vector1 = []
        vector2 = []

        for word, occurrences in corpora:
            vector1.append(occurrences[0])
            vector2.append(occurrences[1])

        return [vector1, vector2]