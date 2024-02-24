#!/usr/bin/env python3
"""
Simple helper function named index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Prototype: def index_range(page:int, page_size: int)
    """
    index = page * page_size - page_size
    index_ = index + page_size
    return (index, index_)
