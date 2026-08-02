from urllib.parse import urlparse, urldefrag


def normalize_url(url):
    url, _ = urldefrag(url)
    return url.rstrip("/")


def is_valid_url(url):
    if not url:
        return False

    if url.startswith("mailto:"):
        return False

    if url.startswith("javascript:"):
        return False

    return url.startswith("http://") or url.startswith("https://")


def is_same_domain(start_url, target_url):
    return urlparse(start_url).netloc == urlparse(target_url).netloc