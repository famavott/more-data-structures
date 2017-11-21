"""Reusable fixtures for tests."""
import pytest


@pytest.fixture
def bst_three():
    """Bst with three nodes."""
    from bst import Tree
    new_tree = Tree((9, 8, 83))
    return new_tree
