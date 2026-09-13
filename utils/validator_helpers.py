"""Data validation and format checking helpers."""

import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
IPV4_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
)
UUID_REGEX = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
)


def is_email(val: str) -> bool:
    """Check if string matches standard email pattern."""
    if not isinstance(val, str) or len(val) > 254:
        return False
    return bool(EMAIL_REGEX.match(val.strip()))


def is_ipv4(val: str) -> bool:
    """Check if string is a valid IPv4 address."""
    if not isinstance(val, str):
        return False
    return bool(IPV4_REGEX.match(val.strip()))


def is_uuid(val: str) -> bool:
    """Check if string is a valid UUID format."""
    if not isinstance(val, str):
        return False
    return bool(UUID_REGEX.match(val.strip()))
