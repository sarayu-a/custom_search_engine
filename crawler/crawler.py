from crawler.downloader import download_page
from crawler.parser import parse_html


def main():
    url = "https://example.com"

    html = download_page(url)

    page = parse_html(html)

    print("\nTitle:")
    print(page["title"])

    print("\nHeadings:")
    for heading in page["headings"]:
        print("-", heading)

    print("\nParagraphs:")
    for paragraph in page["paragraphs"]:
        print("-", paragraph)

    print("\nLinks:")
    for link in page["links"]:
        print("-", link)


if __name__ == "__main__":
    main()