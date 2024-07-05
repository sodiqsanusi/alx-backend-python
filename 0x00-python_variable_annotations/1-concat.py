#!/usr/bin/env python3
"""
More tests on using type annotations in Python code
"""


def concat(str1: str, str2: str) -> str:
    """
    Returns a concatenation of provided string input
    """
    return (f"{str1}{str2}")
