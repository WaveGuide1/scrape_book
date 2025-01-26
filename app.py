import requests

from pages.book_pages import AllBookPage

page_content = requests.get('https://books.toscrape.com/').content

page = AllBookPage(page_content)
books = page.books

for page_number in range(1, page.page_count):
    url = f"https://books.toscrape.com/catalogue/page-{page_number + 1}.html"
    page_content = requests.get(url).content
    page = AllBookPage(page_content)
    books.extend(page.books)
