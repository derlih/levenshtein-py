import platform
import sys
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
        "levdist",
        "from levdist import levenshtein",
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

    return BenchmarkResult(pkg.name, result / ITERATIONS)


def main(
    output: typer.FileTextWrite = typer.Argument(sys.stdout),
    format: OutputFormat = typer.Option(OutputFormat.TEXT),
) -> None:
    with typer.progressbar(PACKAGES) as pkgs:
        results = tuple((benchmark(pkg) for pkg in pkgs))

    if format == OutputFormat.TEXT:
        for result in results:
            typer.echo(f"{result.pkg}: {result.duration / ITERATIONS} sec", output)
    elif format == OutputFormat.MARKDOWN:
        typer.echo(f"# Benchmark ({ITERATIONS} iterations)", output)
        typer.echo(file=output)

        typer.echo("| OS | CPU | Python |", output)
        typer.echo("| -- | --- | ------ |", output)
        typer.echo(
            f"| {platform.system()} {platform.release()} | {platform.processor()} | {sys.version} |",
            output,
        )
        typer.echo(
            """
| Package | Duration of one iteration |
| ------- | ------------------------- |""",
            output,
        )
        for result in results:
            typer.echo(f"| {result.pkg} | {result.duration} |", output)


if __name__ == "__main__":
    typer.run(main)
