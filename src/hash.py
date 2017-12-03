"""Implementation of a hash table."""


class HashTable(object):
    """HashTable class."""

    def __init__(self, size, hash_type='additive'):
        """Create new HashTable object."""
        self.size = size
        self.hash_type = hash_type
        self.buckets = []
        if self.hash_type != 'additive' or self.hash_type != 'oat':
            raise ValueError("Cannot execute given hash type")

    def _hash(self, key):
        """Hash string from user on get method."""
        if self.hash_type == 'additive':
            hash = 0
            for char in key:
                hash += ord(char)
            return hash % self.size
        if self.hash_type == 'oat':
            hash = 0
            for char in key:
                hash += ord(char)
                hash += hash << 10
                hash ^= hash >> 6
            hash += hash << 3
            hash ^= hash >> 11
            hash += hash << 15
            return hash % self.size

    def set(self, key, val):
        """Add a key/val pair to HashTable."""
        idx = self._hash(key)
        pair = [key, val]
        if self.buckets[idx] is None:
            self.buckets[idx] = pair
        else:
            for item in self.buckets[idx]:
                if item[0] == key:
                    item[1] = val
            self.buckets[idx].append[pair]

    def get(self, key):
        """Get value at given key."""
        idx = self._hash(key)
        if self.buckets[idx]:
            for item in self.buckets[idx]:
                if item[0] == key:
                    return item[1]
            raise KeyError('Key not found')
