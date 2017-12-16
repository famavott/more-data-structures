"""Test file for quick sort."""
import pytest


def test_quick_sort_does_not_accept_string():
    """Test if value error raised if str passed in func."""
    from quick_sort import quick_sort
    with pytest.raises(TypeError):
        quick_sort('8, 9, 1, 3')


def test_quick_sort_does_not_accept_tuple():
    """Test if value error raised if tuple passed in func."""
    from quick_sort import quick_sort
    with pytest.raises(TypeError):
        assert quick_sort((8, 9, 1, 3))


def test_empty_list_returns_empty_list():
    """Test if empty list returned given empty list."""
    from quick_sort import quick_sort
    assert quick_sort([]) == []


def test_list_of_one_returns_same_list():
    """Test if list of one returns same list."""
    from quick_sort import quick_sort
    assert quick_sort([9]) == [9]


def test_list_of_two_returns_same_list():
    """Test if list of two swaps."""
    from quick_sort import quick_sort
    assert quick_sort([9, 1]) == [1, 9]


def test_long_list_sorts_in_order():
    """Test if long list prints in correct order."""
    from quick_sort import quick_sort
    assert quick_sort([9, 1, 11, 19, 4, 3, 2, 14]) == [1, 2, 3, 4, 9, 11, 14, 19]


def test_letters_sorted_alphabetically():
    """Test if words are sorted alphabetically."""
    from quick_sort import quick_sort
    words = ['toast', 'eggs', 'syrup', 'bacon']
    assert quick_sort(words) == ['bacon', 'eggs', 'syrup', 'toast']
