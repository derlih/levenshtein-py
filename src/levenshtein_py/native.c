#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdlib.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

static PyObject *method_wagner_fischer(PyObject *self, PyObject *args) {
  const PyObject *a;
  const PyObject *b;

  if (!PyArg_ParseTuple(args, "UU", &a, &b)) {
    PyErr_SetString(PyExc_ValueError, "Can't parse arguments");
    return NULL;
  }

  if (PyUnicode_Compare(a, b) == 0) {
    return PyLong_FromSsize_t(0);
  }

  PyObject *res = NULL;
  const Py_ssize_t len_a = PyUnicode_GetLength(a);
  const Py_ssize_t len_b = PyUnicode_GetLength(b);

  Py_ssize_t *v0 = malloc((len_b + 1) * sizeof(Py_ssize_t));
  if (v0 == NULL) {
    PyErr_SetString(PyExc_SystemError, "Can't allocate buffer");
    return NULL;
  }
  Py_ssize_t *v1 = malloc((len_b + 1) * sizeof(Py_ssize_t));
  if (v1 == NULL) {
    PyErr_SetString(PyExc_SystemError, "Can't allocate buffer");
    goto cleanup;
  }
  for (Py_ssize_t i = 0; i < len_b + 1; i++) {
    v0[i] = i;
  }

  Py_ssize_t *tmp;

  Py_ssize_t deletion_cost, insertion_cost, substitution_cost;
  for (Py_ssize_t i = 0; i < len_a; i++) {
    v1[0] = i + 1;

    for (Py_ssize_t j = 0; j < len_b; j++) {
      deletion_cost = v0[j + 1] + 1;
      insertion_cost = v1[j] + 1;

      if (PyUnicode_ReadChar(a, i) == PyUnicode_ReadChar(b, j)) {
        substitution_cost = v0[j];
      } else {
        substitution_cost = v0[j] + 1;
      }

      v1[j + 1] = MIN(MIN(deletion_cost, insertion_cost), substitution_cost);
    }

    tmp = v0;
    v0 = v1;
    v1 = tmp;
  }
  res = PyLong_FromSsize_t(v0[len_b]);

cleanup:
  free(v0);
  free(v1);
  return res;
}

static PyMethodDef NativeMethods[] = {
    {"wagner_fischer_native", method_wagner_fischer, METH_VARARGS,
     "Python interface for levenshtein.c library"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef nativemodule = {PyModuleDef_HEAD_INIT, "native", NULL,
                                          -1, NativeMethods};

PyMODINIT_FUNC PyInit_native(void) { return PyModule_Create(&nativemodule); }
