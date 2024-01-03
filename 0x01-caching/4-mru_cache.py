#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initializes the cache and sets the last accessed key to an empty string. """
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            # Add the item to the cache
            self.cache_data[key] = item

            # Check if the cache has exceeded its maximum capacity
            if len(self.cache_data) > self.MAX_ITEMS:
                # If so, determine the last accessed key and discard it
                print("DISCARD: {}".format(self.last))
                del self.cache_data[self.last]

            # Update the last accessed key to the current key
            self.last = key

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            # If the key is provided and exists in the cache, update the last accessed key
            self.last = key
            return self.cache_data.get(key)
        # If the key is not provided or doesn't exist in the cache, return None
        return None
