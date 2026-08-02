from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    title = get_title(soup)
    headings = get_headings(soup)
    paragraphs = get_paragraphs(soup)
    links = get_links(soup, base_url)

    return {
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links,
    }


def get_title(soup):
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "No Title"


def get_headings(soup):
    return [
        heading.get_text(strip=True)
        for heading in soup.find_all("h1")
    ]


def get_paragraphs(soup):
    return [
        paragraph.get_text(strip=True)
        for paragraph in soup.find_all("p")
    ]


def get_links(soup, base_url):
    links = []

    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            links.append(urljoin(base_url, href))

    return links