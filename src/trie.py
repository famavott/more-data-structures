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
                    index = curr.child_vals.index(letter)
                    curr = curr.children[index]
            curr.children.append(Node('$', parent=curr))
            curr.child_vals.append('$')
            self._size += 1

        def contains(self, word):
            """Check if word exists in trie."""
            curr = self.root
            for letter in word:
                visited = 0
                for node in curr.children:
                    if letter == node.val:
                        curr = node
                        break
                    visited += 1
                    if visited == len(curr.children):
                        return False
            for node in curr.children:
                if node.val == '$':
                    return True
            return False
