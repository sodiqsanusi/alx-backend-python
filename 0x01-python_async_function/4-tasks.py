#!/usr/bin/env python3
"""
Run multiple asynchronous functions concurrently
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run the 'wait_random' function n times, and get all its values
    asynchronously into a list that will be returned
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    final_list = await asyncio.gather(*tasks)
    return (final_list)
