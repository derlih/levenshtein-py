from .classic import classic

try:
    from .native import wagner_fischer_native as native  # type: ignore
except ImportError:
    pass

from .wagner_fischer import wagner_fischer

__all__ = ["classic", "levenshtein", "native", "wagner_fischer"]


def levenshtein(a: str, b: str) -> int:
    return native(a, b)  # type: ignore[no-any-return]
