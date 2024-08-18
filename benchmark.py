import platform
from dataclasses import dataclass
from enum import Enum
from timeit import timeit

import typer

ITERATIONS = 1_000_000
S1 = "Levenshtein"
S2 = "Frankenstein"
DISTANCE = 6


@dataclass(frozen=True)
class PackageToTest:
    name: str
    setup: str
    call: str


PACKAGES = (
    PackageToTest(
        "levenshtein_py",
        "from levenshtein_py import levenshtein",
        f"levenshtein('{S1}', '{S2}')",
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


@dataclass(frozen=True)
class BenchmarkResult:
    pkg: str
    duration: float


class OutputFormat(str, Enum):
    TEXT = "txt"
    MARKDOWN = "md"


def benchmark(pkg: PackageToTest) -> BenchmarkResult:
    exec(
        f"""
{pkg.setup}
assert {pkg.call} == {DISTANCE}
             """
    )

    result = timeit(
        setup=pkg.setup,
        stmt=pkg.call,
        number=ITERATIONS,
    )

    return BenchmarkResult(pkg.name, result)


def main(format: OutputFormat = OutputFormat.TEXT) -> None:
    with typer.progressbar(PACKAGES) as pkgs:
        results = tuple((benchmark(pkg) for pkg in pkgs))

    if format == OutputFormat.TEXT:
        for result in results:
            typer.echo(f"{result.pkg}: {result.duration / ITERATIONS} sec")
    elif format == OutputFormat.MARKDOWN:
        typer.echo(f"# Benchmark ({ITERATIONS} iterations)")
        typer.echo()
        typer.echo(f"The measurements are done on `{platform.processor()}`")
        typer.echo()
        typer.echo(
            """
| Package | Duration of one iteration |
| ------- | ------------------------- |"""
        )
        for result in results:
            typer.echo(f"| {result.pkg} | {result.duration} |")


if __name__ == "__main__":
    typer.run(main)
