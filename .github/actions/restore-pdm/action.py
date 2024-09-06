import argparse
import os
import subprocess
import sys
from typing import List


def get_cmd_output(*cmd: List[str]) -> str:
    r = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    return r.stdout.decode().strip()


def get_pip_cache_dir() -> str:
    return get_cmd_output("pip", "cache", "dir")


def get_pdm_cache_dir() -> str:
    return get_cmd_output("pdm", "config", "cache_dir")


def get_python_version() -> str:
    return ".".join(str(v) for v in sys.version_info[:3])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("type", choices=["pip", "pdm", "python"])
    args = parser.parse_args()
    with open(os.environ["GITHUB_OUTPUT"], "w") as f:
        if args.type == "python":
            print(f"python-version={get_python_version()}", file=f)
        elif args.type == "pip":
            print(f"pip-cache-dir={get_pip_cache_dir()}", file=f)
        elif args.type == "pdm":
            print(f"pdm-cache-dir={get_pdm_cache_dir()}", file=f)
