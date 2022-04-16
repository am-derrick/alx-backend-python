#!/usr/bin/env python3
"""duck type iterable object"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotates a function's parameters"""
    return [(i, len(i)) for i in lst]
