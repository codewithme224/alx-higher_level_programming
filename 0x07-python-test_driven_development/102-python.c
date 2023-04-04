#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <wchar.h>

/**
 * print_python_string - prints info about Python strings
 * @p: PyObject
 */

void print_python_string(PyObject *p)
{
	PyUnicodeObject *str;
	Py_ssize_t size, i;
	wchar_t *wide_str;

	if (!PyUnicode_check(p))
	{
		printf("Error: Invalid String Object\n");
		return;
	}

	str = (PyUnicodeObject *)p;
	size = PyUnicode_GetLength(p);
	wide_str = PyUnicode_AsWideCharString(p, &size);

	printf("  %ls", wide_str);

	printf("\n  type: %s\n", PyUnicode_GetTypeName((PyObject *)str));
	printf("  length: %zd\n", size);
	printf("  value: %ls\n", wide_str);

	for (i = 0; i < size; i++)
	{
		printf("  %ld: %04x\n", i, wide_str[i]);
	}
}
