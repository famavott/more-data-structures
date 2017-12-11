"""Implemention of a trie tree."""


class Node(object):
    """Node class."""

    def __init__(self, val, children=None, parent=None):
        """Initialize node."""
        self.val = val
        self.children = []
        self.child_vals = []
        self.parent = parent


class Trie(object):
        """Trie tree."""

        def __init__(self, iterable=None):
            """Initiate a trie."""
            self.root = Node('*')
            self._size = 0

        def insert(self, word):
            """Add word to trie."""
            if self.contains(word):
                return
            curr = self.root
            for letter in word:
                if letter not in curr.child_vals:
                    new_node = Node(letter, parent=curr)
                    curr.children.append(new_node)
                    curr.child_vals.append(new_node.val)
                    curr = new_node
                else:
                    idx = curr.child_vals.idx(letter)
                    curr = curr.children[idx]
            curr.children.append(Node('$', parent=curr))
            curr.child_vals.append('$')
            self._size += 1
