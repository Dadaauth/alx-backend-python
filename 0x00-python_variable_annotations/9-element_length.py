#!/usr/bin/env python3
"""A module that works with a lot of functions"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function refactored to contain typing annotations"""
    return [(i, len(i)) for i in lst]
