"""Implementation of binary search tree."""


class Node(object):
    """Create Node class object."""

    def __init__(self, data):
        """Instantiation of Node object."""
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0
        self.parent = None


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
                        new_node.parent = curr
                        self._size += 1
                        break
                    curr = curr.left
                if new_node.data > curr.data:
                    if curr.right is None:
                        new_node.depth = curr.depth + 1
                        curr.right = new_node
                        new_node.parent = curr
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

    def delete(self, data):
        """Remove node from tree if present."""
        if not self.root or not isinstance(data, (int, float)):
            return
        target = self.search(data)
        if not target:
            return
        if not target.left and not target.right:
            self._size -= 1
            if not target.parent:
                self.root = None
            elif target.data > target.parent.data:
                    target.parent.right = None
            else:
                target.parent.left = None
        elif target.left and target.right:
            self._size -= 1
            curr = target.right
            while curr and curr.left:
                curr = curr.left
            if curr.right:
                curr.parent.left = curr.right
            if target.right != curr:
                curr.right = target.right
            curr.left = target.left
            if not target.parent:
                self.root = curr
                curr.parent = None
            else:
                if target.data > target.parent.data:
                    target.parent.right = curr
                else:
                    target.parent.left = curr
                curr.parent = target.parent
        else:
            self._size -= 1
            if target.left:
                child = target.left
            else:
                child = target.right
            if not target.parent:
                self.root = child
                child.parent = None
            else:
                child.parent = target.parent
                if target.data > target.parent.data:
                    target.parent.right = child
                else:
                    target.parent.left = child

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

    def preorder(self):
        """Return values of tree using pre-order traversal."""
        stack = []
        curr = self.root
        while curr:
            curr.right and stack.append(curr.right)
            yield curr.data
            if curr.left:
                curr = curr.left
            else:
                try:
                    curr = stack.pop()
                except IndexError:
                    curr = None

    def breadth_first(self):
        """Return values of tree using breadth first search."""
        stack = []
        curr = self.root
        while curr or stack:
            if curr:
                yield curr.data
                stack.extend([curr.left, curr.right])
                curr = stack.pop(0)
            else:
                curr = stack.pop(0)

    def postorder(self):
        """Return values of tree using post-order search."""
        stack = []
        curr = self.root
        while curr or stack:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and curr.right == stack[-1]:
                    stack.pop()
                    stack.append(curr)
                    curr = curr.right
                else:
                    yield curr.data
                    curr = None


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    tree_a = Tree([97, 77, 72, 70, 62, 48, 40, 30, 13, 9])
    tree_b = Tree([41, 20, 11, 29, 32, 65, 50, 91, 72, 99])

    time_a = ti.timeit("tree_a.search(48)", setup="from __main__ import tree_a")
    time_b = ti.timeit("tree_b.search(65)", setup="from __main__ import tree_b")

    print('Worst case example: {}'.format(time_a))
    print('Best case example: {}'.format(time_b))
