# Find the Maximum element in the entire tree

from collections import deque


class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.right = None
        self.left = None


# Max element with recursion
def maxElement(root):
    if root.left is None and root.right is None:
        return root.val
    return max(maxElement(root.left), maxElement(root.right), root.val)

# Max element with level order
def maxWithLvlOrder(root):
    if root is None:
        return
    myQueue = deque()
    myQueue.append(root)
    arr = []
    while myQueue:
        current = myQueue.popleft()
        arr.append(current.val)
        if current.left:
            myQueue.append(current.left)
        if current.right:
            myQueue.append(current.right)
    return max(arr)

myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)


print(maxElement(myRoot))
print(maxWithLvlOrder(myRoot))