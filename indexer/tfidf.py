import math
from collections import Counter


class TFIDF:

    def __init__(self):
        self.documents = {}

    def add_document(self, document_id, words):
        self.documents[document_id] = Counter(words)

    def search(self, query_words):
        scores = {}

        total_docs = len(self.documents)

        for document_id, counter in self.documents.items():

            score = 0

            for word in query_words:

                tf = counter[word]

                if tf == 0:
                    continue

                df = sum(
                    1 for c in self.documents.values()
                    if word in c
                )

                idf = math.log((total_docs + 1) / (df + 1)) + 1

                score += tf * idf

            if score > 0:
                scores[document_id] = score

        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )