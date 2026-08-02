from crawler.downloader import download_page
from crawler.parser import parse_html
from crawler.queue import URLQueue
from crawler.storage import save_page


def main():
    queue = URLQueue()

    queue.add_url("https://example.com")

    page_number = 1

    while queue.has_urls():

        url = queue.get_url()

        print(f"Crawling: {url}")

        try:
            html = download_page(url)

            save_page(f"page_{page_number}.html", html)

            page = parse_html(html, url)

            print("Title:", page["title"])

            for link in page["links"]:
                queue.add_url(link)

            page_number += 1

            if page_number > 5:
                break

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()