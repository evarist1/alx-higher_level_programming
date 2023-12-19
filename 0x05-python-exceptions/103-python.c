#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item)) {
            printf("bytes\n");
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(item));
            printf("  trying string: %s\n", PyBytes_AsString(item));
            printf("  first 10 bytes: ");
            for (Py_ssize_t j = 0; j < 10 && j < PyBytes_Size(item); ++j) {
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            }
            printf("\n");
        } else if (PyFloat_Check(item)) {
            printf("float\n");
            printf("[.] float object info\n");
            printf("  value: %f\n", PyFloat_AsDouble(item));
        } else if (PyList_Check(item)) {
            printf("list\n");
            print_python_list(item);
        } else if (PyTuple_Check(item)) {
            printf("tuple\n");
            print_python_list(item);
        } else if (PyLong_Check(item)) {
            printf("int\n");
            printf("[.] int object info\n");
            printf("  value: %ld\n", PyLong_AsLong(item));
        } else {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n");
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < 10 && i < PyBytes_Size(p); ++i) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n");
        fprintf(stderr, "  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}
