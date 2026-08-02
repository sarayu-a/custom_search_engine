from crawler.downloader import download_page
from crawler.filters import is_same_domain, is_valid_url
from crawler.parser import parse_html
from crawler.queue import URLQueue
from crawler.storage import save_page
from indexer.search import add_page


MAX_PAGES = 10


def crawl(start_url):
    queue = URLQueue()
    queue.add_url(start_url)

    page_number = 1

    while queue.has_urls() and page_number <= MAX_PAGES:

        current_url = queue.get_url()

        print(f"Crawling: {current_url}")

        try:
            html = download_page(current_url)

            save_page(f"page_{page_number}.html", html)

            page = parse_html(html, current_url)

            text = page["title"] + " " + " ".join(page["paragraphs"])

            add_page(
                f"page_{page_number}",
                text,
                page["title"],
                current_url
            )

            print(f"Title: {page['title']}")

            for link in page["links"]:

                if not is_valid_url(link):
                    continue

                if not is_same_domain(start_url, link):
                    continue

                queue.add_url(link)

            page_number += 1

        except Exception as error:
            print(f"Error: {error}")


def main():
    crawl("https://example.com")


if __name__ == "__main__":
    main()