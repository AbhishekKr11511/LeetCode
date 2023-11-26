# Preorder Traversal

class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.left = None
        self.right = None

# PreOrder Traversal-------------------
def calcPreorder(root):

    # Print first
    print(root.val)
    if root.left:
        calcPreorder(root.left)
    if root.right:
        calcPreorder(root.right)

# PostOrder Traversal------------------
def calcPostorder(root):
    if root.left:
        calcPostorder(root.left)
    if root.right:
        calcPostorder(root.right)

    # Print last
    print(root.val)



# InOrder Traversal--------------------
def calcInorder(root):
    if root.left:
        calcInorder(root.left)

    print(root.val)
    
    if root.right:
        calcInorder(root.right)


# Note : Basically follows the same logic but printing the value of the node is at the top for preorder and at the bottom for postorder and in middle for inorder

myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)


# calcPreorder(myRoot)
# calcPostorder(myRoot)
calcInorder(myRoot)