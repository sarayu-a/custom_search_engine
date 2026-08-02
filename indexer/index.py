from collections import defaultdict


class InvertedIndex:

    def __init__(self):
        self.index = defaultdict(set)
        self.document_frequency = defaultdict(int)

    def add_document(self, document_id, words):

        unique_words = set(words)

        for word in unique_words:
            self.index[word].add(document_id)
            self.document_frequency[word] += 1

    def search(self, word):

        return self.index.get(word, set())