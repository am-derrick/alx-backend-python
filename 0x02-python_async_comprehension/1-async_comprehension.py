#!/usr/bin/env python3
"""async comprehensions"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutines collects 10 random numbers using async comprehension over
    async_generator and returns 10 random numbers"""
    l = [i async for i in async_generator()]
    return l
