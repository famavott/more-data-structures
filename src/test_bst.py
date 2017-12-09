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


def test_contains_returns_true(bst_three):
    """Test contains returns true when value in tree."""
    assert bst_three.contains(9) is True


def test_contains_returns_false(bst_three):
    """Test contains returns true when value in tree."""
    assert bst_three.contains(100) is False


def test_depth_for_one_level(bst_three):
    """Test depth levels for tree of three."""
    assert bst_three.levels == 1


def test_depth_for_two_levels(bst_three):
    """Test depth levels for tree of four."""
    bst_three.insert(6)
    bst_three.levels == 2


def test_depth_if_only_root_exists():
    """Test depth of zero if only root exists."""
    from bst import Tree
    new_tree = Tree(2)
    new_tree.levels == 0


def test_balance_of_even_tree(bst_three):
    """Test balance of balanced tree with three nodes total."""
    bst_three.balance() == 0


def test_balance_greater_on_left(bst_three):
    """Test balance when left is deeper than right."""
    bst_three.insert(6)
    bst_three.balance == 1


def test_balance_greater_on_right(bst_three):
    """Test balance when right is deeper than right."""
    bst_three.insert(17)
    bst_three.balance == -1


def test_balance_negative_two(bst_three):
    """Test balance when right is deeper than right by two levels."""
    bst_three.insert(17)
    bst_three.insert(81)
    bst_three.balance == -2


def test_if_non_int_or_float_passed_raises_error():
    """Test if typeerror is raised when str passed to insert method."""
    from bst import Tree
    new_tree = Tree()
    with pytest.raises(TypeError):
        new_tree.insert('word')


def test_inorder_returns_correct_first_num(big_tree):
    """Test if inorder returns correct digit for big tree."""
    gen_tree = big_tree.inorder()
    assert next(gen_tree) == 2


def test_inorder_full_list_of_nums(big_tree):
    """Test if inorder returns all numbers in tree."""
    gen_tree = big_tree.inorder()
    assert [n for n in gen_tree] == [2, 4, 6, 8, 10, 12, 14, 16]


def test_preorder_returns_correct_first_num(big_tree):
    """Test if preorder returns correct first digit(root)."""
    gen_tree = big_tree.preorder()
    assert next(gen_tree) == 10


def test_preorder_full_list_of_nums(big_tree):
    """Test if preorder returns all numbers in tree."""
    gen_tree = big_tree.preorder()
    assert [n for n in gen_tree] == [10, 6, 4, 2, 8, 12, 16, 14]


def test_bfs_returns_correct_first_num(big_tree):
    """Test if bfs returns correct first digit(root)."""
    gen_tree = big_tree.breadth_first()
    assert next(gen_tree) == 10


def test_bfs_full_list_nums(big_tree):
    """Test if bfs returns all numbers in tree."""
    gen_tree = big_tree.breadth_first()
    assert [n for n in gen_tree] == [10, 6, 12, 4, 8, 16, 2, 14]


def test_first_post_order_yields_correct_num(big_tree):
    """Test if post first num yielded is 2."""
    gen_tree = big_tree.postorder()
    assert next(gen_tree) == 2


def test_second_post_order_gen_yields_correct_num(big_tree):
    """Test if post second num yielded is 4."""
    gen_tree = big_tree.postorder()
    next(gen_tree)
    assert next(gen_tree) == 4


def test_empty_bst_with_postorder_yields_empty_list():
    """Test if empty tree yields empty list."""
    from bst import Tree
    empty_tree = Tree()
    empty_gen = empty_tree.postorder()
    assert [n for n in empty_gen] == []


def test_post_traverses_entire_bst(big_tree):
    """Test if post order traverses tree in correct order."""
    gen_tree = big_tree.postorder()
    assert [n for n in gen_tree] == [2, 4, 8, 6, 14, 16, 12, 10]

  
def test_parent_attr_exits(bst_three):
    """Test value of root that is parent to left child."""
    assert bst_three.root.left.parent.data == 9


def test_parent_attr_nonexistent_for_root(bst_three):
    """Test value of parent of root is none."""
    assert bst_three.root.parent is None


def test_del_empty_tree():
    """Test deletion from empty tree returns None."""
    from bst import Tree
    new_bst = Tree()
    assert new_bst.delete(3) is None


def test_del_nonexistent_val(bst_three):
    """Test deletion of non-existent value returns None."""
    assert bst_three.delete(7) is None


def test_del_root_in_single_node_tree():
    """Test deletion of root in tree of one node."""
    from bst import Tree
    new_bst = Tree()
    new_bst.insert(10)
    new_bst.delete(10)
    assert new_bst.root is None


def test_del_leaf_(bst_three):
    """Test deletion of leaf."""
    bst_three.delete(83)
    assert bst_three.root.right is None
    assert bst_three._size == 2


def test_del_node_with_one_child(big_tree):
    """Test deletion of node with only one child."""
    big_tree.delete(4)
    assert big_tree.root.left.left.data == 2


def test_del_node_with_two_children(big_tree):
    """Test deletion of node with two children."""
    big_tree.delete(6)
    assert big_tree.root.left.left.data == 4


def test_del_root_big_tree(big_tree):
    """Test deletion of root in big tree."""
    big_tree.delete(10)
    assert big_tree.root.data == 12


def test_del_root_right_left_swap(big_tree):
    """Test that root.right.left swaps with root when root deleted."""
    big_tree.insert(11)
    big_tree.delete(10)
    assert big_tree.root.data == 11
