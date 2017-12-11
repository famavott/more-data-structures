"""Test file for trie tree."""
import pytest


def test_node_initialized_with_attrs():
    """Test if node is initialized with attributes."""
    from trie import Node
    new_node = Node('k')
    assert new_node.val == 'k'
