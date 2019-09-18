class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # need to traverse to find spot to insert
    def insert(self, value):
        pass
      # set current node as self
      # while something is true
      # if value is < than node.value and there is a node.left
        # set current node = node.value.left
      # else/if value is >= node.value and there is a node.right
        # set current node = node.value.right
      # else/if value is < than current node.value and there is no current node.left
        # make a new BST with the value
      # else/if value is >= current node.value and there is no current node.right
        # make a new BST with the value

    # `contains` searches the binary search tree for the input value, returning
    # a boolean indicating whether the value exists in the tree or not.
    # starts at root and traverse the tree
    # stop at first instance of a value
    # is not found if we get to a node that doesn't have children
    def contains(self, target):
        pass

    # `get_max` returns the maximum value in the binary search tree.
    def get_max(self):
        pass

    # `for_each` performs a traversal of _every_ node in the tree, executing the
    # passed-in callback function on each tree node value. There is a myriad of
    # ways to perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        pass
      # sets current node value
      # sets compare insert value
      # compares current node value to inserted value
      # if lower go left
        # if no node to left insert
      # else go right
