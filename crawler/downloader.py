import requests

DEFAULT_TIMEOUT = 10


def download_page(url, timeout=DEFAULT_TIMEOUT):
    response = requests.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": (
                "CustomSearchEngine/1.0 "
                "(https://github.com/sarayu-a/custom_search_engine)"
            )
        },
    )

    response.raise_for_status()

    return response.text