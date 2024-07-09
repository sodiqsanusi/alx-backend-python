#!/usr/bin/env python3
"""
Measure the runtime of an async function
"""
import asyncio
from time import time
from typing import Callable
async_comprehension: Callable = __import__(
        '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """
    Run some asynchronous functions and calculate their execution time
    """
    start_time: float = time()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension()
    )
    return time() - start_time
