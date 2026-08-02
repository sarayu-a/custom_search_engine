from indexer.index import InvertedIndex
from indexer.tokenizer import tokenize

_index = InvertedIndex()
_documents = {}


def add_page(document_id, text, title="", url=""):
    words = tokenize(text)
    _index.add_document(document_id, words)

    _documents[document_id] = {
        "title": title,
        "url": url,
        "text": text,
    }


def search(query):
    words = tokenize(query)

    if not words:
        return []

    results = None

    for word in words:
        matches = _index.search(word)

        if results is None:
            results = matches
        else:
            results = results.intersection(matches)

    if not results:
        return []

    return [
        {
            "id": document_id,
            "title": _documents[document_id]["title"],
            "url": _documents[document_id]["url"],
        }
        for document_id in sorted(results)
    ]


def clear():
    _index.clear()
    _documents.clear()