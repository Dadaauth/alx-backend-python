#!/usr/bin/env python3
"""This is my module documentation"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This is my coroutine documentation"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
