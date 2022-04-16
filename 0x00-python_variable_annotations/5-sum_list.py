#!/usr/bin/env python3
"""type-annotated list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list of floats"""
    return sum(input_list)
