from typing import Callable

import pytest

from levdist.classic import classic
from levdist.native import wagner_fischer_native
from levdist.wagner_fischer import wagner_fischer


@pytest.mark.parametrize(
    ("a", "b", "distance"),
    [
        pytest.param("dog", "dog", 0),
        pytest.param("dog", "", 3),
        pytest.param("", "dog", 3),
        pytest.param("kitten", "sitting", 3),
        pytest.param("sitting", "kitten", 3),
        pytest.param("for", "force", 2),
        pytest.param("Levenshtein", "Frankenstein", 6),
        pytest.param("кошка", "кот", 3, id="Unicode"),
        pytest.param("🏉", "🎻", 1, id="Emoji"),
        pytest.param("🏉", "a", 1, id="Strings with different kind"),
    ],
)
@pytest.mark.parametrize("fn", [classic, wagner_fischer, wagner_fischer_native])
def test_distance(a: str, b: str, distance: int, fn: Callable[[str, str], int]):
    assert fn(a, b) == distance
