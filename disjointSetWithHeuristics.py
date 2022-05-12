"""This is a disjoint set implementation with path compression and rank"""

from __future__ import annotations
from typing import Optional, Any, List, Dict


class DisjointSet:
    """This is a disjoint set represented as a tree using dictionary
    Every key in the dictionary represents an item in the disjoint set
    The value is a list of two items. The 0th index is the parent of a particular item and
    second one is its rank.

    -1 in index 0 represents that the node is the rep of set
    """
    items: Optional[Dict]

    def __init__(self):
        self.items = {}

    def make(self, item):
        """Creates a new item for the DS if item does not already exist"""
        if item not in self.items:  # Constant time
            self.items[item] = [-1, 0]

    def find(self, item):
        """Assuming that item is in the disjoint set, this function returns the rep.
        Does path compression"""
        if item not in self.items:
            print("no item")
            return
        # if self.items[item] == -1: # The item is the rep
        #     return item
        # else:
        #     self.find(self.items[item]) # Recursively search for rep of item
        stack = [] # A list that keeps track nodes that were went through for finding
        temp = item
        while self.items[temp][0] != -1:
            stack.append(temp)
            temp = self.items[temp][0]

        for i in stack:
            self.items[i][0] = temp

        return temp

    def union(self, item1, item2):
        """Given item1 and item2 in the disjoint set, union them if in different sets.
        I am making rep of item 2 point to rep of item 1"""
        rep1 = self.find(item1)
        rep2 = self.find(item2)
        if self.items[rep1][1] == self.items[rep2][1]: # Equal ranks join rep2 to rep1
            self.items[rep2][0] = rep1
            self.items[rep1][1] += 1

        elif self.items[rep1][1] < self.items[rep2][1]: # rep1 has lower rank to 1 to 2
            self.items[rep1][0] = rep2

        else:
            self.items[rep2][0] = rep1

    def inSameSet(self, item1, item2):
        """Returns whether item1 and item2 are in the same disjoint set assuming they in ds"""
        return self.find(item1) is self.find(item2)


if __name__ == "__main__":
    ds = DisjointSet()
    ds.make(1)
    ds.make(3)
    ds.make(5)
    ds.make(9)
