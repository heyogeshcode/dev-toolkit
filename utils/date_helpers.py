"""Datetime formatting, parsing, and duration utilities."""

from datetime import datetime, timezone
from typing import Optional


def now_utc_iso() -> str:
    """Return current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).isoformat()


def parse_iso(iso_str: str) -> Optional[datetime]:
    """Safely parse an ISO-8601 formatted string."""
    try:
        return datetime.fromisoformat(iso_str)
    except (ValueError, TypeError):
        return None


def format_readable(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S UTC") -> str:
    """Format datetime to human readable string."""
    return dt.strftime(fmt)


def humanize_seconds(seconds: int) -> str:
    """Convert integer seconds into readable duration string."""
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    rem_sec = seconds % 60
    if minutes < 60:
        return f"{minutes}m {rem_sec}s" if rem_sec else f"{minutes}m"
    hours = minutes // 60
    rem_min = minutes % 60
    return f"{hours}h {rem_min}m"
