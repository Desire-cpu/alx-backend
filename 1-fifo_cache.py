#!/usr/bin/python3
""" FIFOCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            # Add the item to the cache
            self.cache_data[key] = item

            # Check if the cache has exceeded its maximum capacity
            if len(self.cache_data) > self.MAX_ITEMS:
                # If so, determine the item to be removed (FIFO: First In, First Out)
                Delete = sorted(self.cache_data)[0]
                print("DISCARD: {}".format(Delete))
                # Remove the oldest item from the cache
                del self.cache_data[Delete]

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            # If the key is provided and exists in the cache,
            return self.cache_data.get(key)
        # If the key is not provided or doesn't exist in the cache, return None
        return None
