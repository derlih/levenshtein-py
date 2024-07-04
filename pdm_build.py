from distutils.core import Extension
from typing import Any, Dict

from pdm.backend.hooks import Context


def pdm_build_hook_enabled(context: Context) -> None:
    return context.target in ("wheel", "editable")


def pdm_build_update_setup_kwargs(
    context: Context, setup_kwargs: Dict[str, Any]
) -> None:
    sources = [
        "src/levenshtein_py/native.c",
    ]
    setup_kwargs.update(
        ext_modules=[Extension(name="levenshtein_py.native", sources=sources)]
    )
