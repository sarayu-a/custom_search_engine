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

add_page(
    "page3",
    """
    Python and Java are both programming languages.
    """
)

print(search("python"))
print(search("java"))
print(search("python programming"))
print(search("python java"))
print(search("javascript"))