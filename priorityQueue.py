"""
A priority queue using heap implementaiton. This is a max heap
"""
from __future__ import annotations
from typing import Optional, Any, List


class MaxHeap:
    queue: List
    size: int

    def __init__(self):
        self.queue = [None]  # First index is waste
        self.size = 0

    def findMax(self):
        if self.size != 0:
            return self.queue[1]
        else:
            return None

    def insert(self, item):
        self.size += 1
        self.queue.append(item)
        index = self.size
        parent = index // 2
        if self.size == 1:
            return

        while index != 1 and self.queue[parent] < self.queue[index]:
            self.queue[parent], self.queue[index] = self.queue[index], self.queue[parent]
            index = parent
            parent = index // 2

    def extractMax(self):
        root = self.findMax()
        if self.size == 0:
            return None
        if self.size == 1:
            item = self.queue.pop()
            self.size -= 1
            return item

        self.size -= 1
        item = self.queue.pop()
        self.queue[1] = item # Now root is deleted and last item in heap at root

        self.bubbledown(1)
        return root

    def bubbledown(self, index):
        """This function bubbles down the item stored at index assuming children are maxheaps"""
        left = 2 * index
        right = 2 * index + 1
        if left > self.size and right > self.size: # Then no children so done
            return
        elif right > self.size >= left: # No right child only left
            if self.queue[left] >  self.queue[index]:
                self.queue[index], self.queue[left] = self.queue[left], self.queue[index]
            return
        else: # Two children
            largest = index
            if self.queue[largest] < self.queue[left]:
                largest = left
            if self.queue[largest] < self.queue[right]:
                largest = right

            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self.bubbledown(largest)


if __name__ == "__main__":
    pq = MaxHeap()
    pq.insert(5)
    pq.insert(7)
    pq.insert(10)
    pq.insert(1)
