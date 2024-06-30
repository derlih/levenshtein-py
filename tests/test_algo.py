import pytest

from levenshtein_py import recursive


@pytest.mark.parametrize(
    ("a", "b", "distance"),
    [
        pytest.param("dog", "", 3),
        pytest.param("", "dog", 3),
        pytest.param("kitten", "sitting", 3),
    ],
)
def test_distance(a: str, b: str, distance: int):
    assert recursive(a, b) == distance
