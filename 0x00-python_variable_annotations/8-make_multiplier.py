#!/usr/bin/env python3
"""tyep-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns float by multiplier"""
    return (lambda x: multiplier*x)
