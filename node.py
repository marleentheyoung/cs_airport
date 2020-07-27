class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
    
    def get_key(self):
        """Return the key of this node."""
        return self.key
    
    def get_value(self):
        """Return the value of this node."""
        return self.value
    
    def get_parent(self):
        """Return the parent node of this node."""
        return self.parent
    
    def get_left_child(self):
        """Return the left child node of this node."""
        return self.left
    
    def get_right_child(self):
        """Return the right child node of this node."""
        return self.right
    
    def get_height(self):
        """Return the height of this node."""
        return self.height
    
    def update_height(self):
        """Update the height based on the height of the left and right nodes."""
        if self.left == None and self.right == None:
            self.height = 0
        else:
            self.height = max(self.left.height, self.right.height) + 1

    def get_children(self):
        if self.right == None and self.left == None:
            return 0
        return 1
    
    #
    # You can add any additional node functions you might need here
    #
    
    def __eq__(self, other):
        """Returns True if the node is equal the other node or value."""
        if self is other or self.key is other:
            return True
        if (self is None and other is not None):
            return False
        if (other is None and self is not None):
            return False
        if not isinstance(other, int):
            if self.key is other.key:
                return True
        return False
    
    def __neq__(self, other):
        """Returns True if the node is not equal the other node or value."""
        if self is not other:
            return True
        if self.key is not other:
            return True
        return False
    
    def __lt__(self, other):
        """Returns True if the node is less than the other node or value."""
        if isinstance(self, int) and isinstance(other,int):
            if self < other:
                return True
        if self.key < other or self.key < other.key:
            return True
        if self.value is None or other is None:
            return False
        if self.value < other:
            return True
        return False
    
    def __le__(self, other):
        """Returns True if the node is less or equal to the other node or value."""
        if isinstance(self, int) and isinstance(other,int):
            if self <= other:
                return True
        if self.key <= other or self.key <= other.key:
            return True
        if self.value is None or other is None:
            return False
        if self.value <= other:
            return True
        return False
    
    def __gt__(self, other):
        """Returns True if the node is greater than the other node or value."""
        if isinstance(self, int) and isinstance(other,int):
            if self > other:
                return True
        if self.key > other or self.key > other.key:
            return True
        if self.value is None or other is None:
            return False
        if self.value > other:
            return True
        return False
    
    def __ge__(self, other):
        """Returns True if the node is greater or equal to the other node or value."""
        if isinstance(self, int) and isinstance(other,int):
            if self >= other:
                return True
        if self.key >= other or self.key >= other.key:
            return True
        if self.value is None or other is None:
            return False
        if self.value >= other:
            return True
        return False
    
    def __str__(self):
        """Returns the string representation of the node in format: 'key/value'.
           If no value is stored, the representation is just: 'key'."""
        if self.value != None:
            return '{}/{}'.format(self.key, self.value)
        return '{}'.format(self.key)
