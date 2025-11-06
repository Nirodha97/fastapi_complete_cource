from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Title One","author": "Auther One","category": "science"},
    {"title": "Title Two","author": "Auther Two","category": "science"},
    {"title": "Title Three","author": "Auther Three","category": "history"},
    {"title": "Title Four","author": "Auther Four","category": "math"},
    {"title": "Title Five","author": "Auther Five","category": "math"},
    {"title": "Title Six","author": "Auther Six","category": "math"},
]
@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
             return book
    return None


