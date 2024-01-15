
from typing import Any

books_db = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 100,
    }
]

if __name__ == '__main__':
    class Book:
        def __init__(s, id_, name, pages):
            s.id = id_
            s.name = name
            s.pages = pages

        def __str__(s):
            return f"Книга \"{s.name}\""

        def __repr__(s):
            return f"{s.__class__.__name__}(id_={s.id}, name='{s.name}', pages={s.pages})"


    class Library:
        def __init__(s, books=None):
            if books is None:
                s.books = []
            else:
                s.books = books.copy()

        def get_next_book_id(s) -> int:
            return len(s.books) + 1

        def get_index_by_book_id(s, id: Any) -> ValueError | int:
            for index, value in enumerate(s.books):
                if value.id == id:
                    return index
            return ValueError("Книги с запрашиваемым id не существует")


    empty = Library()  
    print(empty.get_next_book_id())  

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in books_db
    ]
    w_books = Library(books=list_books)  
    print(w_books.get_next_book_id())  

    print(w_books.get_index_by_book_id(1))
