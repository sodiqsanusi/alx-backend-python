#!/usr/bin/env python3
"""
Using a regular function, return an asynchronous task
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an async task using asyncio
    """
    return (asyncio.create_task(wait_random(max_delay)))
