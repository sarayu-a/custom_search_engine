from collections import deque


class URLQueue:
    def __init__(self):
        self.queue = deque()
        self.visited = set()

    def add_url(self, url):
        if url not in self.visited:
            self.queue.append(url)
            self.visited.add(url)

    def get_url(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def has_urls(self):
        return len(self.queue) > 0