import logging
import requests

from pages.book_pages import AllBookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO, filename='log.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books...')

page_content = requests.get('https://books.toscrape.com/').content

page = AllBookPage(page_content)
books = page.books

for page_number in range(1, page.page_count):
    url = f"https://books.toscrape.com/catalogue/page-{page_number + 1}.html"
    page_content = requests.get(url).content
    page = AllBookPage(page_content)
    books.extend(page.books)
