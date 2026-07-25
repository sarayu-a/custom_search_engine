import requests


def download_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text