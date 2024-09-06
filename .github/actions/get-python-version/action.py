import os
import sys


def get_python_version() -> str:
    return ".".join(str(v) for v in sys.version_info[:3])


if __name__ == "__main__":
    with open(os.environ["GITHUB_OUTPUT"], "w") as f:
        print(f"python-version={get_python_version()}", file=f)
