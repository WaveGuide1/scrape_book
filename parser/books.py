import re
import logging

from locators.book_locator import BookLocator

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f"Book: {self.name}, £{self.price}, ({self.rating} stars)"

    @property
    def name(self):
        logger.debug('Finding a book name...')
        locator = BookLocator.NAME_LOCATOR
        name = self.parent.select_one(locator).attrs['title']
        logger.debug(f"Found book name `{name}`.")
        return name

    @property
    def link(self):
        logger.debug('Finding a book link...')
        locator = BookLocator.LINK_LOCATOR
        link = self.parent.select_one(locator).attrs['href']
        logger.debug(f"Found book link `{link}`.")
        return link

    @property
    def price(self):
        logger.debug('Finding a book price...')
        locator = BookLocator.PRICE_LOCATOR
        price_link = self.parent.select_one(locator).string

        pattern = '£([0-9]+\\.[0-9]+)'
        price = re.search(pattern, price_link)
        logger.debug(f"Found book price `{price.group(1)}`.")
        return float(price.group(1))

    @property
    def rating(self):
        logger.debug('Finding a book rating...')
        locator = BookLocator.RATING_LOCATOR
        rating_tag = self.parent.select_one(locator).attrs['class']
        rating_class = [r for r in rating_tag if r != 'star-rating']
        logger.debug(f"Found book rating `{rating_class[0]}`.")
        return BookParser.RATINGS.get(rating_class[0])
