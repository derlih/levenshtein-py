from pathlib import Path
from typing import Any, Dict

from Cython.Build import cythonize
from pdm.backend.hooks import Context


def pdm_build_hook_enabled(context: Context) -> None:
    return context.target == "wheel"


def pdm_build_update_setup_kwargs(context: Context, setup_kwargs: Dict[str, Any]):
    src = Path(__file__).parent / "src" / "levenshtein_py" / "two_rows.py"
    setup_kwargs.update(
        ext_modules=cythonize(str(src), compiler_directives={"language_level": "3"})
    )
