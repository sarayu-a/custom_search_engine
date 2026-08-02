from crawler.downloader import download_page
from crawler.parser import parse_html
from indexer.search import add_page

DEFAULT_URL = "https://example.com"


def load_page(url=DEFAULT_URL):
    html = download_page(url)

    page = parse_html(html, url)

    text = page["title"] + " " + " ".join(page["paragraphs"])

    add_page(
        "page_1",
        text,
        title=page["title"],
        url=url,
    )


def main():
    load_page()


if __name__ == "__main__":
    main()