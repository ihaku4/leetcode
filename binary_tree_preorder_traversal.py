# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        res = []
        self.preorderTraversalHelper(root, res)
        return res

    def preorderTraversalHelper(self, node, visited):
        if node:
            visited.append(node.val)
            self.preorderTraversalHelper(node.left, visited)
            self.preorderTraversalHelper(node.right, visited)


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)

        self.root.right = node2
        node2.left = node3
        pass

    def test_default_case(self):
        self.assertEqual([1, 2, 3], Solution().preorderTraversal(self.root))

if __name__ == '__main__':
    unittest.main()
