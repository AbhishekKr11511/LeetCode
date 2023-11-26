'''
Level Order Traversal (or Breadth-First Traversal):

1. Level order traversal visits nodes level by level, starting from the root and moving to the next level before traversing nodes at the same level from left to right.

2. This traversal is typically implemented using a queue data structure.

'''
from collections import deque

class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None


# Here No recursion is required
def levelOrder(root):
    if root is None:
        return 
    lvlQueue = deque()
    lvlQueue.append(root)

    # Run look until empty for every level
    while lvlQueue:
        
        # Use popleft() to pop from the begining, FIFO
        temp  = lvlQueue.popleft()
        print(temp.val)
        if temp.left:
            lvlQueue.append(temp.left)
        if temp.right:
            lvlQueue.append(temp.right)



myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

levelOrder(myRoot)