"""Implementation of binary search tree."""


class Node(object):
    """Create Node class object."""

    def __init__(self, data):
        """Instantiation of Node object."""
        self.data = data
        self.left = None
        self.right = None


class Tree(object):
    """Create Tree class object."""

    def __init__(self, iterable=()):
        """Instantiation of Tree object."""
        self.root = None
        self.size = 0
        if isinstance(iterable, (tuple, list)):
            for data in iterable:
                self.insert(data)

    def insert(self, data):
        """Add a new node to the Tree."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self.size += 1
        curr = self.root
        while curr is not None:
            if new_node.data < curr.data:
                if curr.left is None:
                    curr.left = new_node
                    self.size += 1
                    return
                else:
                    curr = curr.left
            if new_node.data > curr.data:
                if curr.right is None:
                    curr.right = new_node
                    self.size += 1
                    return
                else:
                    curr = curr.right
