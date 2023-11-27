class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.right = None
        self.left = None


def findPath(root, path, val):
    if root is None:
        return False
    
    path.append(root)
    
    if root.val == val:
        return True
    if findPath(root.left, path, val) or findPath(root.right, path, val):
        return True
    
    # If we the above statement return false
    # Then we move to this, meaning there was not any element in that root path, so we pop and check other path
    path.pop()
    return False


def lca(root, node1, node2):
    path1 = []
    path2 = []
    
    if findPath(root, path1, node1) == False or findPath(root, path2, node2) == False:
        return None
    
    [print(path1[i].val, end=" ") for i in range(len(path1))]
    print()
    [print(path2[i].val, end=" ") for i in range(len(path2))]
    print()
    i = 0
    while i < min(len(path1), len(path2)):
        if path1[i] != path2[i]:
            return path1[i-1].val
        i += 1
    return path1[i-1].val

myRoot = Node(10)
myRoot.left = Node(5)
myRoot.right = Node(15)
myRoot.left.left = Node(2.5)
myRoot.left.right = Node(7.5)
myRoot.right.left = Node(12.5)
myRoot.right.right = Node(17.5)

print(lca(myRoot, 12.5, 17.5))