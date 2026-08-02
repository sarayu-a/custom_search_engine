from indexer.index import InvertedIndex
from indexer.tokenizer import tokenize

index = InvertedIndex()

documents = {}


def add_page(document_id, text, title="", url=""):
    words = tokenize(text)
    index.add_document(document_id, words)

    documents[document_id] = {
        "title": title,
        "url": url,
        "text": text
    }


def search(query):
    words = tokenize(query)

    if not words:
        return []

    results = None

    for word in words:
        docs = index.search(word)

        if results is None:
            results = docs
        else:
            results = results.intersection(docs)

    if not results:
        return []

    output = []

    for doc in results:
        output.append({
            "id": doc,
            "title": documents[doc]["title"],
            "url": documents[doc]["url"]
        })

    return output