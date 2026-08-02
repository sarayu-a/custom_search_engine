from indexer.ranker import rank

documents = {
    "page1": "python programming language python",
    "page2": "java programming",
    "page3": "python java programming"
}

results = {"page1", "page3"}

print(rank(results, documents))