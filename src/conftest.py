"""Reusable fixtures for tests."""
import pytest


@pytest.fixture
def bst_three():
    """Bst with three nodes."""
    from bst import Tree
    new_tree = Tree((9, 8, 83))
    return new_tree


@pytest.fixture
def big_tree():
    """Bst with eight nodes."""
    from bst import Tree
    big_tree = Tree((10, 12, 16, 6, 8, 4, 14, 2))
    return big_tree
