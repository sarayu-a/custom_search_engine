from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.load_data import main as load_data
from indexer.search import search

load_data()

app = FastAPI(
    title="Custom Search Engine",
    version="1.0.0",
    description="A simple search engine built with Python and FastAPI.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Custom Search Engine API",
        "status": "running",
    }


@app.get("/search")
def search_api(q: str):
    return {
        "query": q,
        "count": len(search(q)),
        "results": search(q),
    }