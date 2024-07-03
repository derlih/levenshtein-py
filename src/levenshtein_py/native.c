#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "levenshtein.h"

static PyObject *method_native(PyObject *self, PyObject *args) {
  const char *a;
  const char *b;

  if (!PyArg_ParseTuple(args, "ss", &a, &b))
    return NULL;

  const size_t distance = levenshtein(a, b);
  return PyLong_FromSize_t(distance);
}

static PyMethodDef NativeMethods[] = {
    {"levenshtein_native", method_native, METH_VARARGS,
     "Python interface for levenshtein.c library"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef nativemodule = {PyModuleDef_HEAD_INIT, "native", NULL,
                                          -1, NativeMethods};

PyMODINIT_FUNC PyInit_native(void) { return PyModule_Create(&nativemodule); }
