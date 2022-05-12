"""An implementation of a disjoint set adt initially without heuristics
using trees(rep using dict)"""
from __future__ import annotations
from typing import Optional, Any, List, Dict

class DisjointSet:
    """This is a disjoint set represented as a tree using dictionary
    Every key in the dictionary represents an item in the disjoint set
    The value represents the parent of that particular item. You can also do this using an
    actual tree with a hash table where we can directly access the item in that tree

    A -1 value for a key represents that it is the "rep" of that set
    """
    items: Optional[Dict]

    def __init__(self):
        self.items = {}

    def make(self, item):
        """Creates a new item for the DS if item does not already exist"""
        if item not in self.items: # Constant time
            self.items[item] = -1

    def find(self, item):
        """Assuming that item is in the disjoint set, this function returns the rep"""
        if item not in self.items:
            print("no item")
            return
        # if self.items[item] == -1: # The item is the rep
        #     return item
        # else:
        #     self.find(self.items[item]) # Recursively search for rep of item
        temp = item
        while self.items[temp] != -1:
            temp = self.items[temp]

        return temp

    def union(self, item1, item2):
        """Given item1 and item2 in the disjoint set, union them if in different sets.
        I am making rep of item 2 point to rep of item 1"""
        rep1 = self.find(item1)
        rep2 = self.find(item2)
        if rep1 is not rep2:
            self.items[rep2] = rep1

    def inSameSet(self, item1, item2):
        """Returns whether item1 and item2 are in the same disjoint set assuming they in ds"""
        return self.find(item1) is self.find(item2)


if __name__ == "__main__":
    ds = DisjointSet()
    ds.make(1)
    ds.make(3)
    ds.make(5)
    ds.make(9)
