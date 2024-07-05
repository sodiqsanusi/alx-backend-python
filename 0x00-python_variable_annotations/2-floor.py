#!/usr/bin/env python3
"""
More checks on using type annotation, this time with floats
"""
import math


def floor(n: float) -> int:
    """
    Returns a rounded down result of provided float
    """
    return (math.floor(n))
