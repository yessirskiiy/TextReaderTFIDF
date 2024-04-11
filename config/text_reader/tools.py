from math import log


def calculate_tf(document):
    document = document.split()

    word_counts = {}

    for word in document:
        word_counts[word] = word_counts.get(word, 0) + 1
    total_words = len(document)

    tf_values = {word: count / total_words for word, count in word_counts.items()}
    return tf_values


def calculate_idf(document):
    sentences = document.split()

    sentences_words = [sentence.lower().split() for sentence in sentences]
    n = len(sentences_words)

    word_document_counts = {}
    for sentence in sentences_words:
        unique_words = set(sentence)
        for word in unique_words:
            if word:
                word_document_counts[word] = word_document_counts.get(word, 0) + 1

    idf_values = {word: log(n / n_t) for word, n_t in word_document_counts.items() if n_t}
    return idf_values
