"""Test file for bubble sort."""
import pytest


def test_bubble_sort_does_not_accept_string():
    """Test if value error raised if str passed in func."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort('8, 9, 1, 3')


def test_bubble_sort_does_not_accept_tuple():
    """Test if value error raised if tuple passed in func."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort((8, 9, 1, 3))


def test_empty_list_returns_empty_list():
    """Test if empty list returned given empty list."""
    from bubble_sort import bubble_sort
    assert bubble_sort([]) == []


def test_list_of_one_returns_same_list():
    """Test if list of one returns same list."""
    from bubble_sort import bubble_sort
    assert bubble_sort([9]) == [9]


def test_list_of_two_returns_same_list():
    """Test if list of two swaps."""
    from bubble_sort import bubble_sort
    assert bubble_sort([9, 1]) == [1, 9]


def test_long_list_sorts_in_order():
    """Test if long list prints in correct order."""
    from bubble_sort import bubble_sort
    assert bubble_sort([9, 1, 11, 19, 4, 3, 2, 14]) == [1, 2, 3, 4, 9, 11, 14, 19]


def test_letters_sorted_alphabetically():
    """Test if words are sorted alphabetically."""
    from bubble_sort import bubble_sort
    words = ['toast', 'eggs', 'syrup', 'bacon']
    assert bubble_sort(words) == ['bacon', 'eggs', 'syrup', 'toast']
