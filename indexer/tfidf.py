import math
from collections import Counter


class TFIDF:
    def __init__(self):
        self._documents = {}

    def add_document(self, document_id, words):
        self._documents[document_id] = Counter(words)

    def search(self, query_words):
        scores = {}

        total_documents = len(self._documents)

        for document_id, word_counts in self._documents.items():

            score = 0.0

            for word in query_words:

                term_frequency = word_counts[word]

                if term_frequency == 0:
                    continue

                document_frequency = self._document_frequency(word)

                inverse_document_frequency = (
                    math.log((total_documents + 1) / (document_frequency + 1))
                    + 1
                )

                score += term_frequency * inverse_document_frequency

            if score > 0:
                scores[document_id] = score

        return sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

    def _document_frequency(self, word):
        return sum(
            1
            for document in self._documents.values()
            if word in document
        )