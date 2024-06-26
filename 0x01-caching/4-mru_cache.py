#!/usr/bin/env python3
""" MRU caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with an MRU algorithm """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.mru_order.remove(key)
            self.cache_data[key] = item
            self.mru_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.mru_order.pop(-2)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.mru_order.remove(key)
            self.mru_order.append(key)
            return self.cache_data.get(key)
        return None
