#!/usr/bin/env python3
"""async comprehensions"""
from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers using async comprehension over async_generator"""
    l = [i async for i in async_generator()]
    return l
