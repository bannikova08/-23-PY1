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



    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in books_db
    ]
    for book in list_books:
        print(book)

    print(repr(list_books))
