#!/usr/bin/env python3
"""A module containing useful stuffs"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A documentation for this function out of all usefulness."""
    return k, v * v,
