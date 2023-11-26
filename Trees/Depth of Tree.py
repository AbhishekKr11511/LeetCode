class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.left = None
        self.right = None

def maxHeight(root):
    if root is None:
        return 0
    else:
        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)
    
    if leftHeight<rightHeight:
        return rightHeight + 1
    else:
        return leftHeight + 1


# Printing all the nodes present at a certain height
def printNodesAtKHeight(root, k, height=0):
    if root is None:
        return
    if height == k:
        print(root.val)
    
    printNodesAtKHeight(root.left, k, height+1)
    printNodesAtKHeight(root.right, k, height+1)
    

myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)



# print(maxHeight(myRoot))
printNodesAtKHeight(myRoot,4)