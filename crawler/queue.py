from collections import deque

from crawler.filters import normalize_url


class URLQueue:
    def __init__(self):
        self._queue = deque()
        self._visited = set()

    def add_url(self, url):
        url = normalize_url(url)

        if url in self._visited:
            return

        self._visited.add(url)
        self._queue.append(url)

    def get_url(self):
        if not self._queue:
            return None

        return self._queue.popleft()

    def has_urls(self):
        return len(self._queue) > 0

    def size(self):
        return len(self._queue)