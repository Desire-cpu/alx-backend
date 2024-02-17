#!/usr/bin/env python3
"""
Defines a function named `index_range` for pagination calculations.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index corresponding to the range of
    indexes to return in a list for the given pagination parameters.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    start_index = page * page_size
    return start_index - page_size, start_index
