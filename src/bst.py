"""Implementation of binary search tree."""


class Node(object):
    """Create Node class object."""

    def __init__(self, data):
        """Instantiation of Node object."""
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0


class Tree(object):
    """Create Tree class object."""

    def __init__(self, iterable=()):
        """Instantiation of Tree object."""
        self.root = None
        self._size = 0
        self.left_depth = 0
        self.right_depth = 0
        self.levels = 0
        self.left_level = 0
        self.right_level = 0
        if isinstance(iterable, (tuple, list)):
            for data in iterable:
                self.insert(data)
        else:
            self.insert(iterable)

    def insert(self, data):
        """Add a new node to the Tree."""
        if isinstance(data, (int, float)):
            new_node = Node(data)
            if not self.root:
                self.root = new_node
                self._size += 1
                return
            curr = self.root
            while curr:
                if new_node.data < curr.data:
                    if curr.left is None:
                        new_node.depth = curr.depth + 1
                        curr.left = new_node
                        self._size += 1
                        break
                    curr = curr.left
                if new_node.data > curr.data:
                    if curr.right is None:
                        new_node.depth = curr.depth + 1
                        curr.right = new_node
                        self._size += 1
                        break
                    curr = curr.right
            if new_node.depth > self.levels:
                self.levels = new_node.depth
            if new_node.data > self.root.data and new_node.depth > self.right_level:
                self.right_level += 1
            elif new_node.data < self.root.data and new_node.depth > self.left_level:
                self.left_level += 1
        else:
            raise TypeError('Data passed must be an int or float.')

    def search(self, data):
        """Find node with data passed as an argument."""
        curr = self.root
        while curr:
            if curr.data == data:
                return curr
            elif data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right

    def size(self):
        """Return size of Tree."""
        return self._size

    def contains(self, value):
        """Return boolean if value passed is in the tree."""
        return bool(self.search(value))

    def depth(self):
        """Return integer representing number of levels in tree."""
        return self.levels

    def balance(self):
        """Return an integer to determine how balanced the tree is."""
        return self.left_level - self.right_level

    def inorder(self):
        """Return values of tree using in-order traversal."""
        stack = []
        curr = self.root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                yield curr.data
                curr = curr.right


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    tree_a = Tree([97, 77, 72, 70, 62, 48, 40, 30, 13, 9])
    tree_b = Tree([41, 20, 11, 29, 32, 65, 50, 91, 72, 99])

    time_a = ti.timeit("tree_a.search(48)", setup="from __main__ import tree_a")
    time_b = ti.timeit("tree_b.search(65)", setup="from __main__ import tree_b")

    print('Worst case example: {}'.format(time_a))
    print('Best case example: {}'.format(time_b))
