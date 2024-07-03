from dataclasses import dataclass
from timeit import timeit
from typing import Tuple

ITERATIONS = 100_000
S1 = "Levenshtein"
S2 = "Frankenstein"
DISTANCE = 6


@dataclass
class PackageToTest:
    pkg: str
    setup: str
    call: str


if __name__ == "__main__":
    print(f"Benchmark ({ITERATIONS} iterations):")

    packages: Tuple[PackageToTest, ...] = (
        PackageToTest(
            "levenshtein_py",
            "from levenshtein_py import two_rows",
            f"two_rows('{S1}', '{S2}')",
        ),
        PackageToTest(
            "Levenshtein",
            "from Levenshtein import distance",
            f"distance('{S1}', '{S2}')",
        ),
        PackageToTest(
            "python-Levenshtein",
            "from Levenshtein import distance",
            f"distance('{S1}', '{S2}')",
        ),
        PackageToTest(
            "leven",
            "from leven import levenshtein",
            f"levenshtein('{S1}', '{S2}')",
        ),
        PackageToTest(
            "pylev",
            "from pylev import levenshtein",
            f"levenshtein('{S1}', '{S2}')",
        ),
    )

    # Check correctness
    for pkg_to_test in packages:
        exec(
            f"""
{pkg_to_test.setup}
assert {pkg_to_test.call} == {DISTANCE}
             """
        )

    for pkg_to_test in packages:
        result = timeit(
            setup=pkg_to_test.setup,
            stmt=pkg_to_test.call,
            number=ITERATIONS,
        )

        print(f"{pkg_to_test.pkg}: {result/ITERATIONS} sec")
