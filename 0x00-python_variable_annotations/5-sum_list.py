#!/usr/bin/env python3
"""
Use type annotation in lists
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return a sum of the floats in the provided array
    """
    return (sum(input_list))
