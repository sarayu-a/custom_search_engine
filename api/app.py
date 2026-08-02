from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.load_data import main
from indexer.search import search

main()

app = FastAPI()
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
        "message": "Custom Search Engine API"
    }


@app.get("/search")
def search_api(q: str):
    return {
        "query": q,
        "results": search(q)
    }