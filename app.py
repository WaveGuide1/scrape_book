import requests

from pages.book_pages import AllBookPage

page_content = requests.get('https://books.toscrape.com/').content

page = AllBookPage(page_content)
books = page.books
