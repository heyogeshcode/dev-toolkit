"""List, sequence, and dictionary manipulation helpers."""

from typing import Any, Callable, Dict, Iterable, List, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def chunk(items: List[T], size: int) -> List[List[T]]:
    """Split a list into evenly-sized chunks."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i : i + size] for i in range(0, len(items), size)]


def flatten(nested: Iterable[Iterable[T]]) -> List[T]:
    """Flatten an iterable of iterables into a single list."""
    return [item for sublist in nested for item in sublist]


def unique_by(items: Iterable[T], key_fn: Callable[[T], Any]) -> List[T]:
    """Filter items to unique elements based on a key extraction function."""
    seen = set()
    result = []
    for item in items:
        key = key_fn(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def group_by(items: Iterable[T], key_fn: Callable[[T], K]) -> Dict[K, List[T]]:
    """Group items into a dictionary keyed by key_fn."""
    groups: Dict[K, List[T]] = {}
    for item in items:
        k = key_fn(item)
        groups.setdefault(k, []).append(item)
    return groups
