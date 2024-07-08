#!/usr/bin/env python3
"""
Create an async function that can be awaited by an asyncio method
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Gets a random number btw. 0 and inputted param, sleeps for the time
    gotten from the random number
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return (wait_time)
