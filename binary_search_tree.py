# We will have a root node which has a value (5)
# It has two child nodes left and right, and everything that is less than the value goes to the LEFT side and everything greater than
# or equal to will go to the right
# Same rules apply as we go down the tree

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)

tree.inorder_traversal()