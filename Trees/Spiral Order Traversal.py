from collections import deque

class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None
        

leftToRight = True

def spiralOrder(root):
    if root is None:
        return
    stack = []
    stack2 = []
    global leftToRight
    stack2.append(root)
    # Left to right is for stack2
    while stack or stack2:
        if leftToRight:
            while stack2:
                current_stack2 = stack2.pop()
                print(current_stack2.val)
                if current_stack2.left:
                    stack.append(current_stack2.left)
                if current_stack2.right:
                    stack.append(current_stack2.right)
            leftToRight = not leftToRight
            
        # Right to left is for Stack
        else:
            while stack:
                current_stack = stack.pop()
                print(current_stack.val)
                if current_stack.right:
                    stack2.append(current_stack.right)
                if current_stack.left:
                    stack2.append(current_stack.left)
            leftToRight = not leftToRight


myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

myRoot.left.left.left = Node(1)
myRoot.left.left.right = Node(2)
myRoot.left.right.left = Node(3)
myRoot.left.right.right = Node(4)
myRoot.right.left.left = Node(5)
myRoot.right.left.right = Node(6)
myRoot.right.right.left = Node(7)
myRoot.right.right.right = Node(8)

spiralOrder(myRoot)