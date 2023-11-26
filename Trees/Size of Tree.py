# Size of Tree = The number of nodes that are present in the tree

from collections import deque


class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None


# Simple method using recursion
def sizeOfTree(root):
    if root is None:
        return 0

    count = 1 + sizeOfTree(root.left) + sizeOfTree(root.right)
    return count

# Method Using lvl using lvl order
def sizeWithLvlOrder(root):
    if root is None:
        return
    myQueue = deque()
    myQueue.append(root)
    count = 1
    while myQueue:
        current = myQueue.popleft()
        if current.left:
            myQueue.append(current.left)
            count += 1
        if current.right:
            myQueue.append(current.right)
            count += 1
    return count


myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

print(sizeOfTree(myRoot))

print(sizeWithLvlOrder(myRoot))