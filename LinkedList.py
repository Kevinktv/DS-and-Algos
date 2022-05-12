from __future__ import annotations

from typing import Optional, Any


class Node:
    item: Any
    next: Node
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

def buildLinkedList(lst: List) -> Node:
    """Given a list, converts it into a linked list"""
    prev = Node(lst[0])

    for i in range(1, len(lst)):
        temp = Node(i) # Create an empty node
        prev.next = temp
        prev = temp


def search(item: Any, head: Node) -> Node:
    # Given an item and head node in linked list, search for item in linked list
    if head == None:
        return None

    curr = head
    while curr is not None:
        if curr.item == item:
            return True
        else:
            curr = curr.next

    return False
