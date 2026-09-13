"""JSON loading, serialization, and deep merge utilities."""

import json
from typing import Any, Dict, Optional


def safe_loads(raw: str, default: Optional[Any] = None) -> Any:
    """Parse JSON string safely returning default on failure."""
    try:
        return json.loads(raw)
    except (ValueError, TypeError):
        return default


def pretty_dumps(data: Any, indent: int = 2) -> str:
    """Serialize object to formatted JSON string with sorted keys."""
    return json.dumps(data, indent=indent, sort_keys=True)


def deep_merge(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merge dictionary b into a copy of dictionary a."""
    result = dict(dict_a)
    for k, v in dict_b.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result
