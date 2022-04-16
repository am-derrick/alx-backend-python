#!/usr/bin/env pyhton3
"""type-annotated mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[union[int, float]]) -> float:
    """sum of list of floats and integers"""
    return sum(mxd_lst)
