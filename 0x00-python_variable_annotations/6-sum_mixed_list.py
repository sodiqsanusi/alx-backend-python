#!/usr/bin/env python3
"""
More type annotations on list and unions
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes in a list of integers and floats, returns sum of list as float
    """
    return (sum(mxd_lst))
