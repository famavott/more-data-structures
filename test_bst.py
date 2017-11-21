"""Testing for binary search tree."""
import pytest


def test_node_instantiation():
    """Test is Node init is created."""
    test_node = Node(8)
    assert test_node.data == 8
