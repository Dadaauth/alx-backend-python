#!/usr/bin/env python3
"""A docstring to make this module work"""
from typing import Mapping, Any, Union, Type


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[Type, None] = None) -> Union[Any, Type]:
    """A docstring to make this function work"""
    if key in dct:
        return dct[key]
    else:
        return default
