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


@pytest.fixture
def bst_left_imbalanced():
    """Bst that extends left."""
    from bst import BST
    test_bst = BST((10, 9, 8, 7, 6, 5, 4, 3, 2, 1))
    return test_bst


@pytest.fixture
def bst_right_imbalanced():
    """Bst that extends right."""
    from bst import BST
    test_bst = BST((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    return test_bst


@pytest.fixture
def empty_hash():
    """Initialize empty hash table."""
    from hash import HashTable
    test_hash = HashTable()
    return test_hash


@pytest.fixture
def empty_trie():
    """Initialize empty trie."""
    from trie import Trie
    test_trie = Trie()
    return test_trie
