from crawler.downloader import download_page
from crawler.parser import parse_html
from crawler.queue import URLQueue
from crawler.storage import save_page
from crawler.filters import is_valid_url, is_same_domain
from indexer.search import add_page


def main():
    start_url = "https://example.com"

    queue = URLQueue()
    queue.add_url(start_url)

    page_number = 1

    while queue.has_urls():

        url = queue.get_url()

        print(f"Crawling: {url}")

        try:
            html = download_page(url)

            save_page(f"page_{page_number}.html", html)

            page = parse_html(html, url)

            text = " ".join(page["paragraphs"])
            add_page(f"page_{page_number}", text)

            print("Title:", page["title"])

            for link in page["links"]:

                if is_valid_url(link) and is_same_domain(start_url, link):
                    queue.add_url(link)

            page_number += 1

            if page_number > 10:
                break

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()