from .classic import classic
from .wagner_fischer import wagner_fischer

try:
    from .native import wagner_fischer_native  # type: ignore

    def levenshtein(a: str, b: str) -> int:
        return wagner_fischer_native(a, b)  # type: ignore[no-any-return]

except ImportError:
    levenshtein = wagner_fischer

__all__ = ["classic", "levenshtein", "wagner_fischer"]
