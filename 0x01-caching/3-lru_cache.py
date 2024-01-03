#!/usr/bin/python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initializes the cache and sets up an empty history list. """
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            # Add the item to the cache
            self.cache_data[key] = item

            # Check if the cache has exceeded its maximum capacity
            if len(self.cache_data) > self.MAX_ITEMS:
                # If so, determine the least recently used key and discard it
                toDelete = self.history[0]
                print("DISCARD: {}".format(toDelete))
                del self.cache_data[toDelete]
                self.history.pop(0)

            # Update the access history with the current key
            self.updateHistory(key)

    def get(self, key):
        """ Get an item by key """
        if key and key in self.cache_data:
            # If the key is provided and exists in the cache, update the access history
            self.updateHistory(key)
            return self.cache_data.get(key)
        # If the key is not provided or doesn't exist in the cache, return None
        return None

    def updateHistory(self, key):
        """ Updates cache history """
        if key in self.history:
            # If the key is already in the history, remove it
            self.history.remove(key)
        # Append the current key to the end of the history list
        self.history.append(key)
