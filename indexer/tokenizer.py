import re

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "in", "on", "at", "to", "of", "for", "and",
    "or", "with", "by", "this", "that", "it"
}

WORD_PATTERN = re.compile(r"\b[a-zA-Z]+\b")


def tokenize(text):
    words = extract_words(text)
    return remove_stop_words(words)


def extract_words(text):
    return WORD_PATTERN.findall(text.lower())


def remove_stop_words(words):
    return [
        word
        for word in words
        if word not in STOP_WORDS
    ]