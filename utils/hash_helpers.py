"""Hashing, checksum, and secure token generation utilities."""

import hashlib
import secrets


def sha256_hex(data: str) -> str:
    """Compute hex encoded SHA-256 hash of a string."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def md5_hex(data: str) -> str:
    """Compute hex encoded MD5 checksum of a string."""
    return hashlib.md5(data.encode("utf-8")).hexdigest()


def generate_token(byte_length: int = 32) -> str:
    """Generate a cryptographically secure URL-safe token."""
    return secrets.token_urlsafe(byte_length)
