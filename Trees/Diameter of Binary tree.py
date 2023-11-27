class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None
    

def heightOfTree(root):
    if root is None:
        return 0
    else:
        leftTree = heightOfTree(root.left)
        rightTree = heightOfTree(root.right)

    return max(leftTree, rightTree) + 1
    
def diameterOfTree(root):

    return heightOfTree(root.left) + heightOfTree(root.right) + 1


myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

print(diameterOfTree(myRoot))