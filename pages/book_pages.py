import re
import logging
from bs4 import BeautifulSoup

from locators.book_page_locator import AllBookPageLocator
from parser.books import BookParser

logger = logging.getLogger('scraping.all_book_pages')


class AllBookPage:

    def __init__(self, page_content):
        logger.debug('Passing page content with beautifulSoup Html Parser')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBookPageLocator.BOOKS}`.')
        locator = AllBookPageLocator.BOOKS
        return [BookParser(b) for b in self.soup.select(locator)]

    @property
    def page_count(self):
        logger.debug('Finding the number of catalogue pages available...')
        content = self.soup.select_one(AllBookPageLocator.PAGES).string
        logger.info(f'Found number of catalogue pages available... `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted page number in integer `{pages}`.')
        return pages