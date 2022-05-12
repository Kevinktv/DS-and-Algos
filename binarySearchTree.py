from __future__ import annotations
from typing import Optional, Any


class BinarySearchTree:
    root: Optional[Any]
    left: Optional[BinarySearchTree]
    right: Optional[BinarySearchTree]

    def __init__(self, root: Any) -> None:
        if root == None:
            self.root = None
            self.left = None
            self.right = None
        else:
            self.root = root
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)

    def isEmpty(self):
        return self.root is None

    def search(self, item):
        if self.isEmpty():
            return False

        else:
            if item == self.root:
                return True
            elif item < self.root:
                self.left.search(item)
            else:
                self.right.search(item)

    def insert(self, item):
        if self.isEmpty():
            self.root = item
            self.left = BinarySearchTree(None)
            self.right = BinarySearchTree(None)

        elif item < self.root:
            self.left.insert(item)
        else:
            self.right.insert(item)

    def delete(self, item):
        if self.isEmpty():
            pass
        else:
            if item < self.root:
                self.left.delete(item)
            elif item > self.root:
                self.right.delete(item)
            else:
                self.deleteRoot()

    def deleteRoot(self):
        if self.left.isEmpty() and self.right.isEmpty():
            self.left = None
            self.right = None
            self.root = None
        elif self.left.isEmpty(): # Right is not empty
            self.root, self.left, self.right = self.right.root, self.right.left, self.right.right

        elif self.right.isEmpty():
            # "Promote" the left subtree.
            self.root, self.left, self.right = self.left.root, self.left.left, self.left.right
        else: # Need predecessor
            self.root = self.left.extractAndRemoveMax()

    def extractAndRemoveMax(self):
        temp = self
        while not self.right.isEmpty():
            temp = self.right

        val = temp.root
        temp.root, temp.left, temp.right = temp.left.root, temp.left.left, temp.left.right
        return val

    def inOrder(self):
        """Prints the tree contents in order (left, root, right)"""
        if self.left is not None:
            self.left.inOrder()

        if self.root is not None:
            print(self.root)

        if self.right is not None:
            self.right.inOrder()

if __name__ == "__main__":
    tree = BinarySearchTree(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(8)
    tree.inOrder()
    tree.delete(5)
    tree.inOrder()
