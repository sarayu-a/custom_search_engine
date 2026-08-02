from crawler.queue import URLQueue

queue = URLQueue()

queue.add_url("https://example.com")
queue.add_url("https://google.com")
queue.add_url("https://example.com")

while queue.has_urls():
    print(queue.get_url())