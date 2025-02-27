import logging

from app import books

logger = logging.getLogger('scraping.menu')

CHOICE = """ Enter one of the following choices:
- 'b' 5-Star Books
- 'c' Cheapest books
- 'd' Ten best Highest rated books
- 'e' Ten best High-rated Cheapest books
- 'n' Get the next available book on the catalogue
- 'q' To exit
Enter your choice: """


def ten_best_books():
    logger.info('Finding best ten books...')
    sorted_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in sorted_books:
        print(book)


def five_star_books():
    logger.info('Finding best ten five star rating books...')
    sorted_books = filter(lambda x: x.rating == 5, books)
    for book in sorted_books:
        print(book)


def ten_cheapest_books():
    logger.info('Finding ten cheapest books...')
    sorted_books = sorted(books, key=lambda x: x.price)[:10]
    for book in sorted_books:
        print(book)


def ten_best_and_cheapest_books():
    logger.info('Finding ten cheapest and best books...')
    sorted_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in sorted_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info('Finding books individually...')
    print(next(books_generator))


USER_CHOICES = {
    'b': five_star_books,
    'c': ten_cheapest_books,
    'd': ten_best_books,
    'e': ten_best_and_cheapest_books,
    'n': get_next_book
}

def book_menu():
    user_input = input(CHOICE).lower()
    while user_input != 'q':
        if user_input in {'b', 'c', 'd', 'e', 'n'}:
            USER_CHOICES[user_input]()
            user_input = input(CHOICE).lower()
        else:
            print("Please choose a valid command")
            user_input = input(CHOICE).lower()


book_menu()
