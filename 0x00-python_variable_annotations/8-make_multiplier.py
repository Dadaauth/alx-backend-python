#!/usr/bin/env python3
"""A module containing an important function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A docstring for the multiplier function maker"""
    def multiplier_func(n: float) -> float:
        """The main mutplier function"""
        return n * multiplier
    return multiplier_func
