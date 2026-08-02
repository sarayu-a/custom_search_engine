from collections import Counter


def rank(results, documents):
    scores = Counter()

    for document_id in results:
        text = documents.get(document_id, "").lower()

        scores[document_id] = calculate_score(text)

    return sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )


def calculate_score(text):
    words = text.split()

    return len(words)