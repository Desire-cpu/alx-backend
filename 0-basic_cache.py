#!/usr/bin/python3
""" BasicCache module """
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            # If both key and item are provided, add the item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            # If the key is provided and exists in the cache, return the corresponding item
            return self.cache_data.get(key)
        # If the key is not provided or doesn't exist in the cache, return None
        return None
