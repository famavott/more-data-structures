"""Test file for trie tree."""
import pytest


def test_node_initialized_with_attrs():
    """Test if node is initialized with attributes."""
    from trie import Node
    new_node = Node('k')
    assert new_node.val == 'k'


def test_trie_intialized_with_root(empty_trie):
    """Test if root is '*' on initialization."""
    assert empty_trie.root.val == '*'


def test_trie_size_initalized_zero(empty_trie):
    """Test if size is zero on initalization."""
    assert empty_trie._size == 0


def test_inserting_word_into_empty_trie(empty_trie):
    """Test if word added into empty tree."""
    empty_trie.insert('ball')
    assert empty_trie.root.children[0].val == 'b'


def test_insert_two_words(empty_trie):
    """Two nodes with same first letters."""
    empty_trie.insert('ball')
    empty_trie.insert('balk')
    l = empty_trie.root.children[0].children[0]
    assert l.children[0].val == 'l'
    assert l.children[0].children[1].val == 'k'


def test_contains_if_word_in_trie(empty_trie):
    """Test if word in trie returns true."""
    empty_trie.insert('ball')
    assert empty_trie.contains('ball') is True


def test_contains_if_word_not_in_trie(empty_trie):
    """Test if word in trie returns true."""
    empty_trie.insert('balance')
    assert empty_trie.contains('ball') is False


def test_size(empty_trie):
    """Test if size with multiple words inserted returns number."""
    empty_trie.insert('balance')
    empty_trie.insert('ball')
    empty_trie.insert('balk')
    empty_trie.insert('ansible')
    assert empty_trie._size == 4


def test_size_with_remove(empty_trie):
    """Test if size after remove returns correct number."""
    empty_trie.insert('balance')
    empty_trie.insert('ball')
    empty_trie.insert('balk')
    empty_trie.insert('ballfield')
    empty_trie.remove('ball')
    assert empty_trie._size == 3


def test_remove_raises_error_if_not_present(empty_trie):
    """Riase ValueError if word in in tree."""
    empty_trie.insert('balance')
    empty_trie.insert('ball')
    empty_trie.insert('balk')
    with pytest.raises(ValueError):
        empty_trie.remove('ballfield')
