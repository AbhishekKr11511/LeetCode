# Print the left most value at each lvl in a binary tree

from collections import deque

class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.left = None
        self.right = None


# Declare the global variable
maxlevel = 0

def leftView(root, currentlvl=1):

    # Use the global keyword to indicate that you are using the global variable
    global maxlevel
    if root is None:
        return
    
    # If the function has visited that level, it won't enter, So the first value which is the left most is always printed
    if currentlvl>maxlevel:
        print(root.val)
        # If printed update the maxlevel
        maxlevel = currentlvl
    
    leftView(root.left, currentlvl+1)
    leftView(root.right, currentlvl+1)





yourRoot = Node(10)
yourRoot.left = Node(5)
yourRoot.right = Node(15)
yourRoot.left.left = Node(2.5)
yourRoot.left.right = Node(7.5)
yourRoot.right.left = Node(12.5)
yourRoot.right.right = Node(17.5)

myRoot = Node(20)
myRoot.left = Node(70)
myRoot.right = Node(90)
myRoot.right.left = Node(30)
myRoot.right.right = Node(70)
myRoot.right.left.right = Node(10)

ourRoot = Node(20)
ourRoot.right = Node(90)
ourRoot.right.left = Node(30)
ourRoot.right.left.right = Node(10)

leftView(yourRoot)