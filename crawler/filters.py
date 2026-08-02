from urllib.parse import urldefrag, urlparse


def normalize_url(url):
    url, _ = urldefrag(url)
    return url.rstrip("/")


def is_valid_url(url):
    if not url:
        return False

    url = normalize_url(url)

    if url.startswith(("mailto:", "javascript:", "tel:")):
        return False

    return url.startswith(("http://", "https://"))


def is_same_domain(start_url, target_url):
    return (
        urlparse(start_url).netloc.lower()
        == urlparse(target_url).netloc.lower()
    )