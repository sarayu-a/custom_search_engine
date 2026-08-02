from collections import defaultdict


class InvertedIndex:

    def __init__(self):
        self.index = defaultdict(set)

    def add_document(self, document_id, words):

        for word in words:
            self.index[word].add(document_id)

    def search(self, word):

        return self.index.get(word, set())