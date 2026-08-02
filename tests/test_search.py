from indexer.search import add_page, search


add_page(
    "page1",
    """
    Python is a programming language.
    Python is used for web development.
    """
)

add_page(
    "page2",
    """
    Java is another programming language.
    """
)

print(search("python"))
print(search("java"))
print(search("javascript"))