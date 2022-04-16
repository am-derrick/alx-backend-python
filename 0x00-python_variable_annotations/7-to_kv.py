#!/usr/bin/env python3
"""type-annotated string and int/float to tuple function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a tring and int/float and returns a tuple"""
    return (k, v ** 2)
