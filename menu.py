from app import books

CHOICE = """ Enter one of the following choice:
- 'b' 5-Star Books
- 'c' Cheapest books
- 'd' Ten best Highest rated books
- 'e' Ten best High-rated Cheapest books
- 'n' Get the next available book on the catalogue
- 'q' To exit
Enter your choice: """


def ten_best_book():
    sorted_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in sorted_books:
        print(book)


def five_star_books():
    sorted_books = filter(lambda x: x.rating == 5, books)
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


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


def book_menu():
    while True:
        user_input = input(CHOICE).lower()
        if user_input == 'q':
            print("BYE.......")
            break
        if user_input == 'b':
            five_star_books()
        elif user_input == 'c':
            ten_cheapest_book()
        elif user_input == 'd':
            ten_best_book()
        elif user_input == 'e':
            ten_best_and_cheapest_book()
        elif user_input == 'n':
            get_next_book()
        else:
            print("Please choose a valid command")
            continue


book_menu()
