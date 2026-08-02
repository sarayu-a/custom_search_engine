from fastapi import FastAPI
from api.load_data import main
from indexer.search import search

main()

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Custom Search Engine API"
    }


@app.get("/search")
def search_api(q: str):
    return {
        "query": q,
        "results": list(search(q))
    }