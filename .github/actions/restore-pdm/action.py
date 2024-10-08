import argparse
import os
import subprocess
from typing import List


def get_cmd_output(*cmd: List[str]) -> str:
    r = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    return r.stdout.decode().strip()


def get_uv_cache_dir() -> str:
    return get_cmd_output("uv", "cache", "dir")


def get_pdm_cache_dir() -> str:
    return get_cmd_output("pdm", "config", "cache_dir")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("type", choices=["pip", "uv", "pdm"])
    args = parser.parse_args()
    with open(os.environ["GITHUB_OUTPUT"], "w") as f:
        if args.type == "uv":
            print(f"uv-cache-dir={get_uv_cache_dir()}", file=f)
        elif args.type == "pdm":
            print(f"pdm-cache-dir={get_pdm_cache_dir()}", file=f)
