#!/usr/bin/env python3
""" LRU caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with an LRU algorithm """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lru_order.remove(key)
            self.cache_data[key] = item
            self.lru_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data.get(key)
        return None
