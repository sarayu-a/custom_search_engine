from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self._index = defaultdict(set)
        self._document_frequency = defaultdict(int)

    def add_document(self, document_id, words):
        unique_words = set(words)

        for word in unique_words:
            self._index[word].add(document_id)
            self._document_frequency[word] += 1

    def search(self, word):
        return self._index.get(word, set())

    def get_document_frequency(self, word):
        return self._document_frequency.get(word, 0)

    def contains(self, word):
        return word in self._index

    def clear(self):
        self._index.clear()
        self._document_frequency.clear()