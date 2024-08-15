from typing import Any, Dict

from Cython.Build import cythonize
from mypyc.build import mypycify
from pdm.backend.hooks import Context
from setuptools import Extension


def pdm_build_hook_enabled(context: Context) -> None:
    return context.target in ("wheel", "editable")


def pdm_build_update_setup_kwargs(
    context: Context, setup_kwargs: Dict[str, Any]
) -> None:
    native_ext = Extension(
        name="levenshtein_py.native",
        sources=["src/levenshtein_py/native.c"],
    )
    cython_exts: list[Extension] = cythonize(
        [
            Extension(
                name="levenshtein_py.cython",
                sources=["src/levenshtein_py/wagner_fischer.py"],
            )
        ]
    )
    mypyc_exts = mypycify(["src/levenshtein_py/mypyc.py"])

    setup_kwargs.update(
        ext_modules=[
            native_ext,
            *cython_exts,
            *mypyc_exts,
        ]
    )
