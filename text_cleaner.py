import re


def clean_text(text):
    text = text.lower()

    # Keep letters, numbers, and common technical symbols
    text = re.sub(r"[^a-z0-9+#.\-/ ]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()