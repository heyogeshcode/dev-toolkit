"""String formatting and processing utility functions."""

import re
from typing import List


def slugify(text: str) -> str:
    """Convert a text string to URL-safe slug format."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Safely truncate text to max_length including suffix."""
    if len(text) <= max_length:
        return text
    if max_length <= len(suffix):
        return text[:max_length]
    return text[: max_length - len(suffix)] + suffix


def split_words(text: str) -> List[str]:
    """Split text into words removing excess whitespace."""
    return re.findall(r"\b\w+\b", text)
