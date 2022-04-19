#!/usr/bin/env python3
"""run time for parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    """coroutine that executes async_comprehension four times in prallel
    using asyncio.gather and measures total runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop = time.perf_counter()
    return stop - start
