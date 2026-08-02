from bs4 import BeautifulSoup


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string if soup.title else "No Title"

    headings = [heading.get_text(strip=True) for heading in soup.find_all("h1")]

    paragraphs = [paragraph.get_text(strip=True) for paragraph in soup.find_all("p")]

    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)

    return {
        "title": title,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links,
    }