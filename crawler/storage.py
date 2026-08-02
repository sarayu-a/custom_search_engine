import os


def save_page(filename, html):
    os.makedirs("data", exist_ok=True)

    path = os.path.join("data", filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write(html)