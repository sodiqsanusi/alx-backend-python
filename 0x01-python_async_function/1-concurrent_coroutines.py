#!/usr/bin/env python3
"""
Run multiple asynchronous functions concurrently
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run the 'wait_random' function n times, and get all its values
    asynchronously into a list that will be returned
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    final_list = await asyncio.gather(*tasks)
    return (final_list)
