import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)

        if value >= self.value:
                if not self.right:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if target == self.value return it
        if target == self.value:
            return True
        # go left or right if smaller or bigger
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.right.contains(target)

        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach (use recursion if you can ALSO:
    #   @@@COMEBACK@@@ AND TRY iterative to see the difference.)
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)  

        ##Iteratively -- use stack
        #   stack = Stack()
        #   stack.push(self)

        #   while stack.length > 0:
        #       current_node = stack.pop()
        #       if current_node.right:
        #            stack.push(current_node.right)
        #       if current_node.left:
        #            stack.push(current_node.left)
        #            cb(current_node.value)

    # DAY 2 Project -----------------------

    # **Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        

    # **Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        

    # **Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        pass
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
    sums = 3
