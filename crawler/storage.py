from pathlib import Path

DATA_DIRECTORY = Path("data")


def save_page(filename, html):
    DATA_DIRECTORY.mkdir(exist_ok=True)

    file_path = DATA_DIRECTORY / filename

    file_path.write_text(html, encoding="utf-8")