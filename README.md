[![Build Status](https://travis-ci.org/famavott/more-data-structures.svg?branch=master)](https://travis-ci.org/famavott/more-data-structures)

# Data Structures

## Binary Search Tree
A data structure made up of nodes where each node has no more than two child nodes. The left child is always less in value than the parent, and the right child is always greater in value than the parent.

Insert(self, data): Adds a node to the tree with the data passed. If node with data is already in tree, it will be ignored.

Time Complexity: O(n)

Search(self, data): Returns node containing that value, else None.

Time Complexity: O(n)

Size(self): Returns the integer size of the tree.

Time Complexity: O(1)

Depth(self): Returns an integer of the total number of levels in the tree. If there is one value, then depth is 0, if two values, then depth is 1, and so on.

Time Complexity: O(1)

Contains(self, data): Returns True if value is present in tree, and False if it is not.

Time Complexity: O(n)

Balance(self): Returns an interger denoting the balance of the tree. Trees that are skewed right will return a positive value, while trees skewed left will return a negative value. Balanced trees will return 0.

Time Complexity: O(1)

## Binary Search Tree Traversals

In-Order(self): Returns a generator that will return the values in the tree using in-order traversal, one at a time.

Time Complexity: O(n)

Pre-Order(self): Returns a generator that will return the values in the tree using pre-order traversal, one at a time.

Time Complexity: O(n)

Breadth-First(self): Returns a generator that will return the values in the tree using breadth-first traversal, one at a time.

Time Complexity: O(n)

Post-Order(self): Returns a generator that will return the values in the tree using post_order traversal, one at a time.

Time Complexity: O(n)

## Binary Search Tree Deletion

Delete(self, data): Removes a value if present, otherwise returns nothing. Returns None in all cases.

Time Complexity: O(n)

## Hash Table

hash(self, data): Hashes the key provided, and executes either additive, or one-at-time based on input.

Time Complexity: O(n)

set(self, key, val): Adds a key/value pair to the table. Overwrites the existing value if key is already present.

Time Complexity: O(n)

get(self, key): Returns value associated with key. Raises an error if key is not found.

Time Complexity: O(n)

## Trie
