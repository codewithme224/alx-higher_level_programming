#!/usr/bin/python3
"""Module for lazy_matrix_mul function"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices by using the module NumPy"""
    return np.matmul(m_a, m_b)
