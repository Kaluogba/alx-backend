#!/usr/bin/env python3
""" LFU caching """

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with an LFU algorithm """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.lfu_count = defaultdict(int)
        self.lfu_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.lfu_order.remove(key)
            self.cache_data[key] = item
            self.lfu_count[key] += 1
            self.lfu_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lfu_key = min(self.lfu_order, key=lambda k: (
                    (self.lfu_count[k], self.lfu_order.index(k)))
                    )
                del self.cache_data[lfu_key]
                del self.lfu_count[lfu_key]
                self.lfu_order.remove(lfu_key)
                print("DISCARD: {}".format(lfu_key))

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.lfu_count[key] += 1
            self.lfu_order.remove(key)
            self.lfu_order.append(key)
            return self.cache_data.get(key)
        return None
