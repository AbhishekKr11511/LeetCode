Understanding binary trees in data structures and algorithms is crucial, and having a solid grasp of key formulas and concepts can indeed help you solve problems more efficiently. Here are some key points and formulas related to binary trees:

**Height `h` starts from `0`**

1. **Height of a Binary Tree (or Depth):**
   - The height of a binary tree is the length of the longest path from the root to a leaf node.
   - Formula: `height(root) = 1 + max(height(leftSubtree), height(rightSubtree))`
   - The height of an empty tree is usually considered to be -1.

2. **Number of Nodes in a Full Binary Tree:**
   - In a full binary tree, every node has either 0 or 2 children.
   - The number of nodes `N` in a full binary tree with height `h` is given by: `N = 2^(h+1) - 1`

3. **Number of Nodes in a Complete Binary Tree:**
   - In a complete binary tree, all levels are completely filled except possibly for the last level, which is filled from left to right.
   - The number of nodes `N` in a complete binary tree with height `h` can vary but is between `2^h` and `2^(h+1) - 1`.

4. **Minimum and Maximum Height of a Binary Tree with `n` Nodes:**
   - For a binary tree with `n` nodes, the minimum height is `log2(n+1) - 1`.
   - The maximum height is `n - 1`.

5. **Types of Binary Trees:**
   - **Full Binary Tree:** A binary tree in which every node has 0 or 2 children.
   - **Complete Binary Tree:** A binary tree in which all levels are completely filled except possibly for the last level, which is filled from left to right.
   - **Perfect Binary Tree:** A binary tree in which all leaf nodes are at the same level.
   - **Balanced Binary Tree:** A binary tree in which the depth of the left and right subtrees of every node differ by at most one.

6. **Binary Tree Traversal:**
   - **Inorder (LNR):** Traverse the left subtree, visit the root, traverse the right subtree.
   - **Preorder (NLR):** Visit the root, traverse the left subtree, traverse the right subtree.
   - **Postorder (LRN):** Traverse the left subtree, traverse the right subtree, visit the root.

7. **Binary Search Tree (BST):**
   - A binary search tree is a binary tree in which the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree only nodes with keys greater than the node's key.

8. **Formula for the Number of Binary Trees with `n` Nodes:**
   - The number of structurally unique binary trees with `n` nodes (unordered) is given by the nth Catalan number: `Cn = (2n)! / ((n+1)! * n!)`

Understanding these concepts and formulas will be beneficial for solving problems related to binary trees. Practice implementing and working with binary trees through coding exercises to solidify your understanding.