"""Implementation of a hash table."""


class HashTable(object):
    """HashTable class."""

    def __init__(self, size=10, hash_type='additive'):
        """Create new HashTable object."""
        self.size = size
        self.hash_type = hash_type
        self.buckets = []
        if hash_type not in ('additive', 'oat'):
            raise NameError('Hash funciton unsupported')
        for i in range(size):
            self.buckets.append([])

    def _hash(self, key):
        """Hash string from user on get method."""
        if type(key) is not str:
            raise TypeError('Key must be a string')
        if self.hash_type == 'additive':
            hash = 0
            for char in key:
                hash += ord(char)
            print(hash % self.size)
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
            print(hash % self.size)
            return hash % self.size

    def set(self, key, val):
        """Add a key/val pair to HashTable."""
        idx = self._hash(key)
        pair = [key, val]
        if not self.buckets[idx]:
            self.buckets[idx].append(pair)
        else:
            for item in self.buckets[idx]:
                if item[0] == key:
                    item[1] = val
            self.buckets[idx].append(list(pair))

    def get(self, key):
        """Get value at given key."""
        idx = self._hash(key)
        if self.buckets[idx]:
            for item in self.buckets[idx]:
                if item[0] == key:
                    return item[1]
        raise KeyError('Key not found')
