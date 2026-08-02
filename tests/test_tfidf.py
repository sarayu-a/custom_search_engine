from indexer.tfidf import TFIDF
from indexer.tokenizer import tokenize

engine = TFIDF()

engine.add_document(
    "page1",
    tokenize("python python programming language")
)

engine.add_document(
    "page2",
    tokenize("java programming")
)

engine.add_document(
    "page3",
    tokenize("python java programming")
)

print(engine.search(tokenize("python")))