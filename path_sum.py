# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        nodeStack = [(root, root.val)]

        while len(nodeStack) > 0:
            n, nSum = nodeStack.pop()

            if n.left is None and \
               n.right is None and \
               nSum == sum:
                return True
            if n.left is not None:
                nodeStack.append((n.left, nSum + n.left.val))
            if n.right is not None:
                nodeStack.append((n.right, nSum + n.right.val))
        return False

    def _hasPathSum(self, root, sum):
        if root is None:
            return False

        nodeStack = [root]
        sumStack = [root.val]

        while len(nodeStack) > 0:
            n = nodeStack.pop()
            nSum = sumStack.pop()

            if n.left is None and \
               n.right is None and \
               nSum == sum:
                return True
            if n.left is not None:
                nodeStack.append(n.left)
                sumStack.append(nSum + n.left.val)
            if n.right is not None:
                nodeStack.append(n.right)
                sumStack.append(nSum + n.right.val)
        return False


root = TreeNode(5)

rootl = TreeNode(4)
rootr = TreeNode(8)
root.left = rootl
root.right = rootr

# 3rd level
rootll = TreeNode(11)
rootl.left = rootll

rootrl = TreeNode(13)
rootrr = TreeNode(4)
rootr.left = rootrl
rootr.right = rootrr

# 4th level
rootlll = TreeNode(7)
rootllr = TreeNode(2)
rootll.left = rootlll
rootll.right = rootllr

rootrrr = TreeNode(1)
rootrr.right = rootrrr

s = Solution()
print s.hasPathSum(root, 22)
