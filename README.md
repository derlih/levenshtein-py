# levenshtein-py

A Python package to calculate the Levinstein distance algorithm implementation with non-GPL license, typing and speedups.
The implementation is based on code samples from [Levenstein Wiki](https://en.wikipedia.org/wiki/Levenshtein_distance).

## Installation

`pip install levenshtein-py`

## Usage

```python
from levenstein_py import levenshtein

distance = levenstein("dog", "cat")
```

## Development

#### Setup

1. Install PDM using [this](https://pdm-project.org/latest/#installation) documentation
2. Install development dependencies `pdm install`
3. Install `pre-commit` hooks `pre-commit install`

#### Testing

This project is using `pytest` for unit testing.
To run the test you need to run `pdm test`
In addition to that you can lint your code using `pdm lint` and check the typing by `pdm mypy`.

#### Type checks

`mypy` is configured to run in strict mode for files in `src` folder. Typing is not checked in `tests` folder.

#### CI

##### PR checks

Each PR run GitHub actions for all actual Python versions to check if native extension is built and tests pass.
Also formatting and typing will be checked.

The coverage is published to CodeCov.

##### Dependency updates

To update dependencies and `pre-commit` hooks there is a GHA job that is scheduled to run weekly.

##### Release

To create a release, create a tag `v<MAJOR>.<MINOR>.<PATCH>`. The [release](https://github.com/derlih/levenshtein-py/releases) will be created with the source code and wheels.

## Benchmark

The benchmark of this package can be run using `pdm benchmark` command. It compare its speed with other Python implementations.
Check the [BENCHMARK.md](BENCHMARK.md) for the latest measurements.
