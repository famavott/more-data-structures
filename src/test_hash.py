"""Testing for hash table tree."""
import pytest


def test_hash_initialized(empty_hash):
    """Test if hash table initailized with attributes."""
    assert empty_hash.size == 10
    assert empty_hash.hash_type == 'additive'


def test_hash_initiailized_custom_size():
    """Test if hash table can be initailized with custom size."""
    from hash import HashTable
    cust_hash = HashTable(size=100)
    cust_hash.size == 100


def test_hash_initialized_with_oat():
    """Test if hash table can be initialized using oat hashing function."""
    from hash import HashTable
    cust_hash = HashTable(hash_type='oat')
    cust_hash.hash_type == 'oat'


def test_bad_hash_type_raises_error():
    """Test if ValueError raised if function other than additive or oat is passed."""
    from hash import HashTable
    with pytest.raises(NameError):
        HashTable(hash_type='something')


def test_non_string_passed_in_set_raises_error(empty_hash):
    """Type error raised when non-string passed in set method."""
    with pytest.raises(TypeError):
        empty_hash.set(897, 'toast')


def test_set_adds_pair(empty_hash):
    """Test if set adds to key/val pair to bucket."""
    empty_hash.set('potato', 8)
    assert empty_hash.buckets[3] == [['potato', 8]]


def test_get_returns_correct_val(empty_hash):
    """Test if correct val returned for get method."""
    empty_hash.set('jim', 39)
    assert empty_hash.get('jim') == 39


def test_key_can_be_updated_with_new_val(empty_hash):
    """Test if key's value can be updated."""
    empty_hash.set('jim', 39)
    empty_hash.set('jim', 83)
    assert empty_hash.get('jim') == 83


def test_key_not_found_error_raises(empty_hash):
    """Test if KeyError raised when get used for key not in table."""
    empty_hash.set('jane', 34)
    empty_hash.set('andy', 32)
    with pytest.raises(KeyError):
        empty_hash.get('bob')
