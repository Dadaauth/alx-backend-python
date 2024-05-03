#!/usr/bin/env python3
"""A module to work on 👍"""
from typing import Any, Sequence, Union, Optional, Type
type NoneType = (None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """A docstring for this function"""
    if lst:
        return lst[0]
    else:
        return None
