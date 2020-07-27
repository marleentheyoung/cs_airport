from node import Node
from collections import *

class BST(object):
    def __init__(self, key_list=[]):
        """Create a new BST, set its attributes, and insert all the keys in
           the key_list into the BST."""
        self.key_list = key_list
        self.root = None
        self.nodes = {}
        self.traverse = None
        self.level = []

        # Connect Nodes
        for key in key_list:
            self.insert(key)

    
    def get_root(self):
        """Return the root of the BST."""
        return self.root
    
    def is_empty(self):
        """Return True if the BST is empty."""
        if self.root == None:
            return True
        return False
    
    def find_max(self):
        """Return the node with the maximum key in the BST."""
        return max(self.nodes, key=int)

    
    def find_min(self):
        """Return the node with the minimum key in the BST."""
        return min(self.nodes, key=int)
    
    def search(self, key):
        """Return the Node object containing the key if the key exists in
           the BST, else return None."""
        if key in self.key_list:
            return (self.nodes)[key]
        return None
    
    def contains(self, key):
        """ Return True if the key exists in the BST, else return False."""
        if key in self.key_list:
            return True
        return False
    
    def insert(self, key, value=None):
        """Create a new node for this key and value, and insert it into the BST.
           
           Return the new inserted node, or None if the key and value could not
           be inserted."""
        if key in self.nodes:
            return None
        else:
            new_node = Node(key, value)
            (self.nodes)[key] = new_node          
            current = self.root
            last = current

            if current is None:
                self.root = self.nodes[key]
                self.root.height = 0
                return new_node

            while (current is not None):
                if new_node.key > current.key:
                    last = current
                    current = current.right
                    if (current != None and current.left == None) or (current == self.root):
                            current.height += 1
                else:
                    last = current
                    current = current.left
                    if (current != None and current.left == None) or (current == self.root):
                            current.height += 1

            if new_node.key > last.key:
                last.right = new_node
                new_node.parent = last
            else:
                last.left = new_node
                new_node.parent = last

            self.root.height = self.get_height_tree()
            return new_node

    def get_height_tree(self):
        """ Returns height of tree, i.e. height of root node."""
        layers = self.breadth_first_traversal()
           
        if all(node is None for node in layers[-1]):
            del layers[-1]
        
        height = len(layers) - 1
        return height

    def is_full(self, node):
        """Checks if a given node has both a left child and right child."""
        if node.right != None and node.left != None:
            return True
        return False


    def is_leaf(self, node):
        if node == None:
            return False
        elif node.get_children() == 0:
            return True

    def find_successor(self, node):
        """Find the inorder successor of a given node. Function should be 
            used for deleting nodes from a tree.
        """  
        current_node = node

        if current_node.right != None:
            current_node = current_node.right
            while current_node.get_children() != 0:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            return current_node
        else:
            return None

    def delete_root(self, node):
        """Deletes root node from BST tree."""
        current = node
        successor = self.find_successor(current) 
        temp_height = current.height
        current.height = successor.height
        successor.height = temp_height

        if successor != None:
            self.root = successor
            parent = successor.parent

            if successor.parent != node:
                if parent.left == successor:
                    parent.left = successor.left
                else:
                    parent.right = successor.right
            if node.left != successor:
                successor.left = node.left
            else:
                successor.left = None
            if node.right != successor:
                successor.right = node.right 
            else:
                successor.right = None

        else:
            ancestor = node.left
            ancestor.parent = None
            self.root = ancestor
        del self.nodes[node.key]

    def delete_one_child(self, node):
        """Deletes node from tree if it has only one child."""
        if node.left != None:
            child = node.left
        else:
            child = node.right
                
        parent = node.parent
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child
        child.parent = parent
        del self.nodes[node.key]

        self.update_path(parent)

    def delete_leaf(self, node):
        """Deletes leaf node."""
        parent = node.get_parent()
        if node == parent.left:
            parent.left = None
        if node == parent.right:
            parent.right = None
        del (self.nodes)[node.key]

        if parent.get_children() == 0:
            self.update_path(parent)

    def delete(self, key):
        """Remove the Node object containing the key if the key exists in
           the BST and return the removed node, else return None.
           
           The returned node is the actual Node object that got removed
           from the BST, and so might be successor of the removed key."""
        if key in self.nodes:
            node = self.nodes[key]        
            if node == self.root:
                root = True
            else:
                root = False

            if node.get_children() == 0:
                leaf = True
            else:
                leaf = False
                if (node.left != None and node.right != None):
                    one_child = False
                else:
                    one_child = True

            # get connected nodes to reconnect them in the tree
            parent_node = node.get_parent()

            if root == True:
                self.delete_root(node)
            
            elif leaf == True:
                self.delete_leaf(node)

            elif one_child == True:
                self.delete_one_child(node)

            elif root == False:
                current = node

                while current.right.get_children() != 0:
                    current = current.right

                    if current.right == None:
                        break
                current = current.left
                parent = current.parent
                if parent.right == current:
                    parent.right = current.right
                    current.right.parent = parent
                else:
                    parent.left = current.right
                    current.right.parent = parent

                if parent_node.left == node:
                    parent_node.left = current
                else:
                    parent_node.right = current
                current.parent = parent_node
                current.left = node.left
                node.left.parent = current
                node.right.parent = current
                current.right = node.right

                del self.nodes[key]
            return node
        return None

    def update_path(self, parent):
        """Updates all parent nodes above a given node, using the update
           height function"""
        parent.update_height()

        while (parent != self.root):
            parent = parent.parent
            parent.update_height()
        

    def in_order_traversal(self):
        """Returns an in order ordered list of all nodes in the tree by
           recursively traversing nodes."""
        root = self.root
        self.traverse = self.in_order_traversal_node(root)
        return self.traverse
   

    def in_order_traversal_node(self, node):
        ordered = []
        if node:
            ordered = self.in_order_traversal_node(node.left) 
            ordered.append(node)
            ordered = ordered + self.in_order_traversal_node(node.right)
        return ordered

    
    def breadth_first_traversal(self):
        """Return a list of lists, where each inner lists contains the elements
           of one layer in the tree. Layers are filled in breadth-first-order,
           and contain contain all elements linked in the BST, including the
           None elements.
           >> BST([5, 8]).breadth_first_traversal()
           [[Node(5)], [None, Node(8)], [None, None]]"""
        breadth_first = []
        h = self.root.get_height() 
        for i in range(h+2): 
            self.level = []
            self.print_level(self.root, i + 1) 
            breadth_first.append(self.level)
        return breadth_first   
    
    # Print nodes at a given level 
    def print_level(self, node , level): 
        """Prints one depth level of the tree."""
        if node is None and level == 1: 
            self.level.append(None)
        elif node != None:
            # set the root level as the base case
            if level == 1: 
                self.level.append(node)
            elif level > 1 : 
                self.print_level(node.left , level - 1) 
                self.print_level(node.right , level - 1) 
        return self.level
            

    
    def __str__(self):
        """Return a string containing the elements of the tree in breadth-first
           order, with each on a new line, and None elements as `_`, and
           finally a single line containing all the nodes in sorted order.
           >> print(BST([5, 8, 3]))
           5
           3 8
           _ _ _ _
           3 5 8
           """
        current = self.root
        nodes = [self.root]
        final = str(self.root) + "\n"
        count = 0
        while len(nodes) != 0:
            count += 1
            if count == 10:
                return ""
            temp = []
            for node in nodes:
                if node.left != None:
                    temp.append(node.left)
                    final += str(node.left) + " "
                else:
                    final += "_ "
                if node.right != None:
                    temp.append(node.right)
                    final += str(node.right) + " "
                else:
                    final += "_ "
                if temp == []:
                    if node == nodes[len(nodes) - 1]:
                        break
            final += "\n"
            nodes = temp
        self.in_order_traversal()
        for item in self.traverse:
            final += str(item.key) + " "
        final += "\n"
        return final

        

