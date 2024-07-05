#!/usr/bin/env python3
"""
Module testing type annotations on Lists and Unions
"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple after operations have taken place on input
    """
    return k, v ** 2
