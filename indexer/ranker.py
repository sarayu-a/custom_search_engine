from collections import Counter


def rank(results, documents):
    scores = Counter()

    for document in results:
        text = documents.get(document, "").lower()

        for word in text.split():
            scores[document] += 1

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)