from crawler.downloader import download_page


def main():
    url = "https://example.com"

    html = download_page(url)

    print(html[:500])


if __name__ == "__main__":
    main()