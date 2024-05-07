#!/usr/bin/env python3
"""This is my module documentation"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This is my coroutine documentation"""
    task = [asyncio.create_task(wait_random(max_delay))
            for _ in range(n)]
    return [await task for task in asyncio.as_completed(task)]
