"""Color code conversion and luminance calculation utilities."""

from typing import Tuple


def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    """Convert hex color string to (r, g, b) integer tuple."""
    hex_clean = hex_code.lstrip("#")
    if len(hex_clean) == 3:
        hex_clean = "".join(c * 2 for c in hex_clean)
    if len(hex_clean) != 6:
        raise ValueError(f"Invalid hex color format: {hex_code}")
    return tuple(int(hex_clean[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB integers to 6-character hex color string."""
    for val, name in ((r, "r"), (g, "g"), (b, "b")):
        if not 0 <= val <= 255:
            raise ValueError(f"{name} must be between 0 and 255")
    return f"#{r:02x}{g:02x}{b:02x}"


def relative_luminance(r: int, g: int, b: int) -> float:
    """Calculate perceived relative luminance according to WCAG formula."""
    channels = []
    for c in (r, g, b):
        norm = c / 255.0
        channels.append(norm / 12.92 if norm <= 0.03928 else ((norm + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]
