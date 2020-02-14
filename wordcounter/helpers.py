import nltk
from collections import defaultdict


def count_and_sort_words(text):
    parsed_text = nltk.word_tokenize(text.lower())
    word_counts = defaultdict(int)
    for word in parsed_text:
        word_counts[word] += 1
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
