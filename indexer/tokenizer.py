import re


def tokenize(text):
    text = text.lower()

    words = re.findall(r"\b[a-zA-Z]+\b", text)

    return words