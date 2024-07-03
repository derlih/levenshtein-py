from dataclasses import dataclass
from timeit import timeit
from typing import Tuple

ITERATIONS = 100_000
S1 = "Levenshtein"
S2 = "Frankenstein"


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
            "from levenshtein_py import full_matrix",
            f"full_matrix('{S1}', '{S2}')",
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

    for pkg_to_test in packages:
        result = timeit(
            setup=pkg_to_test.setup,
            stmt=pkg_to_test.call,
            number=ITERATIONS,
        )

        print(f"{pkg_to_test.pkg}: {result/ITERATIONS} sec")
