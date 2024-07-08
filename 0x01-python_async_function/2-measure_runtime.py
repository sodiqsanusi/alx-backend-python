#!/usr/bin/env python3
"""
Calculate the time spent running the asyncronous tasks
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Get the execution time of an asynchronous function and make computations
    based on the results
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    execution_time = end_time - start_time
    return (execution_time / n)
