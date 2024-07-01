from pathlib import Path

from mypyc.build import mypycify


def pdm_build_hook_enabled(context):
    return context.target == "wheel"


def pdm_build_update_setup_kwargs(context, setup_kwargs):
    src_dir = Path(__file__).parent / "src" / "levenshtein_py"
    files_to_mypyc = [str(f) for f in src_dir.glob("*.py")]
    setup_kwargs.update(
        ext_modules=mypycify(["--strict", *files_to_mypyc], verbose=True)
    )
