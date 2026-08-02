from crawler.downloader import download_page
from crawler.parser import parse_html
from indexer.search import add_page


def main():
    url = "https://example.com"

    html = download_page(url)

    page = parse_html(html, url)

    text = page["title"] + " " + " ".join(page["paragraphs"])

    add_page("page_1", text)