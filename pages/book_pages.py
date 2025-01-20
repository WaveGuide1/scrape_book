from bs4 import BeautifulSoup

from locators.book_page_locator import AllBookPageLocator
from parser.books import BookParser


class AllBookPage:

    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        locator = AllBookPageLocator.BOOKS
        return [BookParser(b) for b in self.soup.select(locator)]