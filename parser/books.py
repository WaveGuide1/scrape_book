import re

from locators.book_locator import BookLocator


class BookParser:

    RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Book: {self.name}, £{self.price}, ({self.rating} stars)"

    @property
    def name(self):
        locator = BookLocator.NAME_LOCATOR
        return self.parent.select_one(locator).attrs['title']

    @property
    def link(self):
        locator = BookLocator.LINK_LOCATOR
        return self.parent.select_one(locator).attrs['href']

    @property
    def price(self):
        locator = BookLocator.PRICE_LOCATOR
        price_link = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        price = re.search(pattern, price_link)
        return float(price.group(1))

    @property
    def rating(self):
        locator = BookLocator.RATING_LOCATOR
        rating_tag = self.parent.select_one(locator).attrs['class']
        rating_class = [r for r in rating_tag if r != 'star-rating']
        return BookParser.RATINGS.get(rating_class[0])
