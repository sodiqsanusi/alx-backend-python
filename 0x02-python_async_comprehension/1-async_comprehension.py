#!/usr/bin/env python3
"""
Use asynchronous comprehension to get results from an async generator
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Get values from an async generator
    return result as a list using comprehension
    """
    lilac = [i async for i in async_generator()]
    return (lilac)
