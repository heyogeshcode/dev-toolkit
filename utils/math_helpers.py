"""Mathematical and numeric calculation utilities."""

from typing import List, Union

Number = Union[int, float]


def clamp(val: Number, min_val: Number, max_val: Number) -> Number:
    """Clamp a value within min and max boundaries."""
    return max(min_val, min(val, max_val))


def lerp(start: Number, end: Number, t: float) -> float:
    """Linear interpolation between two values."""
    return start + (end - start) * clamp(t, 0.0, 1.0)


def mean(numbers: List[Number]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: List[Number]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_nums[mid])
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
