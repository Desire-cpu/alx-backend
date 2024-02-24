#!/usr/bin/env python3
"""
Simple pagination: index_range
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Fetches and caches the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data based on the specified page and page size.
        Arguments: page (int), page_size (int)
        """
        assert isinstance(page_size, int) and isinstance(page, int)
        assert page > 0
        assert page_size > 0
        self.dataset()
        index_range_result = index_range(page, page_size)
        if index_range_result[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[index_range_result[0]:index_range_result[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Computes the index range for a given page and page size.
    Returns a tuple (start_index, end_index).
    """
    start_index = page * page_size - page_size
    end_index = start_index + page_size
    return (start_index, end_index)
