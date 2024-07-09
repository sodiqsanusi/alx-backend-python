#!/usr/bin/env python3
"""
Create an asynchronous function generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Loop a number of times, waiting asynchronously between each loop
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
