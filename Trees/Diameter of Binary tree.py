class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None
    
# This is the function that gets the height from the specific node
def heightOfTree(root):
    if root is None:
        return 0
    else:
        leftTree = heightOfTree(root.left)
        rightTree = heightOfTree(root.right)

    return max(leftTree, rightTree) + 1

# This function returns the diamter of that specific node
def diameterOfTree(root):
    return heightOfTree(root.left) + heightOfTree(root.right) + 1

# This stores all the possible diameters of the tree
arrDiameter = []

# This traverses through the tree to get the diameter from each node
def maxDiameter(root):
    global arrDiameter
    if root is None:
        return
    arrDiameter.append(diameterOfTree(root))
    if root.left:
        maxDiameter(root.left)
    if root.right:
        maxDiameter(root.right)
    
    # Finally we return the maximum diameter possible
    return max(arrDiameter)

# First Tree
myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

# Second Tree
thisRoot = Node(1)
thisRoot.left = Node(2)
thisRoot.right = Node(3)
thisRoot.left.left = Node(4)
thisRoot.left.right = Node(5)
thisRoot.left.left.left = Node(6)
thisRoot.left.left.right = Node(7)
thisRoot.left.left.left.left = Node(9)
thisRoot.left.right.right = Node(8)
thisRoot.left.right.right.right = Node(10)

print(maxDiameter(myRoot))
print(maxDiameter(thisRoot))