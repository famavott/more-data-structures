"""Test file for radix sort."""
import pytest


def test_radix_does_not_accept_string():
    """Test if value error raised if str passed in func."""
    from radix import radix
    with pytest.raises(TypeError):
        radix('8, 9, 1, 3')


def test_radix_does_not_accept_tuple():
    """Test if value error raised if tuple passed in func."""
    from radix import radix
    with pytest.raises(TypeError):
        assert radix((8, 9, 1, 3))


def test_list_of_one_returns_same_list():
    """Test if list of one returns same list."""
    from radix import radix
    assert radix([9]) == [9]


def test_list_of_two_returns_same_list():
    """Test if list of two swaps."""
    from radix import radix
    assert radix([9, 1]) == [1, 9]


def test_long_list_sorts_in_order():
    """Test if long list prints in correct order."""
    from radix import radix
    assert radix([9, 1, 11, 19, 4, 3, 2, 14]) == [1, 2, 3, 4, 9, 11, 14, 19]
