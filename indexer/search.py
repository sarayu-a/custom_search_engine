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

    return index.search(words[0])