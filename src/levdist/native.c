#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdlib.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

static PyObject *method_wagner_fischer(PyObject *self, PyObject *args) {
  PyObject *a;
  PyObject *b;

  if (!PyArg_ParseTuple(args, "UU", &a, &b)) {
    PyErr_SetString(PyExc_ValueError, "Can't parse arguments");
    return NULL;
  }

  const Py_ssize_t len_a = PyUnicode_GetLength(a);
  const Py_ssize_t len_b = PyUnicode_GetLength(b);

  if (len_a == 0) {
    return PyLong_FromSsize_t(len_b);
  }

  if (len_b == 0) {
    return PyLong_FromSsize_t(len_a);
  }

  if (len_a == len_b && PyUnicode_Compare(a, b) == 0) {
    return PyLong_FromSsize_t(0);
  }

  int kind_a = PyUnicode_KIND(a);
  void *data_a = PyUnicode_DATA(a);
  int kind_b = PyUnicode_KIND(b);
  void *data_b = PyUnicode_DATA(b);

  Py_ssize_t *v = malloc(2 * (len_b + 1) * sizeof(Py_ssize_t));
  if (v == NULL) {
    PyErr_SetString(PyExc_SystemError, "Can't allocate buffer");
    return NULL;
  }

  Py_ssize_t *v0 = v;
  Py_ssize_t *v1 = v + len_b + 1;

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

      if (PyUnicode_READ(kind_a, data_a, i) ==
          PyUnicode_READ(kind_b, data_b, j)) {
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

  PyObject *res = PyLong_FromSsize_t(v0[len_b]);
  free(v);
  return res;
}

static PyMethodDef NativeMethods[] = {
    {"wagner_fischer_native", method_wagner_fischer, METH_VARARGS,
     "Python interface for levenshtein.c library"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef nativemodule = {PyModuleDef_HEAD_INIT, "native", NULL,
                                          -1, NativeMethods};

PyMODINIT_FUNC PyInit_native(void) { return PyModule_Create(&nativemodule); }
