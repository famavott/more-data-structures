"""Testing for binary search tree."""
import pytest


def test_node_initialized():
    """Test if Node is created."""
    from bst import Node
    test_node = Node(8)
    assert test_node.data == 8


def test_tree_initialized():
    """Test if Tree is created."""
    from bst import Tree
    test_tree = Tree()
    test_tree.size = 0


def test_tree_initialized_with_one_argument():
    """Test if one node created when tree is initialized."""
    from bst import Tree
    test_tree = Tree(3)
    test_tree.root.data == 3


def test_tree_size_attr_after_nodes_inserted(bst_three):
    """Test if size of tree increases to three after nodes inserted."""
    assert bst_three._size == 3


def test_root_after_three_nodes_added(bst_three):
    """Test if root is correct after adding three nodes."""
    assert bst_three.root.data == 9
    assert bst_three.root.left.data == 8
    assert bst_three.root.right.data == 83


def test_search_for_root(bst_three):
    """Test if root node is returned if passed as argument."""
    assert bst_three.search(9).data == 9


def test_search_for_left_node(bst_three):
    """Test if left node data is returned."""
    assert bst_three.search(8) is bst_three.root.left


def test_search_for_nonexistent_data(bst_three):
    """Test if return is None when looking for non-existent data."""
    assert bst_three.search(99) is None


def test_size_method_with_three_nodes(bst_three):
    """Test if size method returns correct size."""
    assert bst_three.size() == 3


def test_size_method_with_no_nodes():
    """Test if size method returns zero when no nodes in Tree."""
    from bst import Tree
    new_tree = Tree()
    new_tree.size() == 0
