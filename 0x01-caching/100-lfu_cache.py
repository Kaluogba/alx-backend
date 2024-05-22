#!/usr/bin/env python3
""" LFU Caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system with LFU eviction policy
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}
        self.lru = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.lru[key] = self.lru_counter
            self.lru_counter += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                min_keys = [k for k, v in self.frequency.items()(
                    if v == min_freq]
                    )
                lru_key = min(min_keys, key=lambda k: self.lru[k])
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.lru[lru_key]

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.lru[key] = self.lru_counter
            self.lru_counter += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.lru[key] = self.lru_counter
        self.lru_counter += 1
        return self.cache_data[key]

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = {}
        self.lru = {}
        self.lru_counter = 0
