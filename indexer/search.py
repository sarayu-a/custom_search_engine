from indexer.index import InvertedIndex
from indexer.tokenizer import tokenize

index = InvertedIndex()


def add_page(document_id, text):
    words = tokenize(text)
    index.add_document(document_id, words)


def search(query):
    words = tokenize(query)

    if not words:
        return set()

    results = None

    for word in words:
        docs = index.search(word)

        if results is None:
            results = docs
        else:
            results = results.intersection(docs)

    return results if results else set()