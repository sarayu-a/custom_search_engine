import re

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "in", "on", "at", "to", "of", "for", "and",
    "or", "with", "by", "this", "that", "it"
}


def tokenize(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return [word for word in words if word not in STOP_WORDS]