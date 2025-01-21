from app import books


def ten_best_book():
    sorted_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in sorted_books:
        print(book)


def ten_cheapest_book():
    sorted_books = sorted(books, key=lambda x: x.price)[:10]
    for book in sorted_books:
        print(book)


def ten_best_and_cheapest_book():
    sorted_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in sorted_books:
        print(book)


ten_best_and_cheapest_book()
