# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        # return self.DFS(root)
        return self.BFS(root)

    def BFS(self, root):
        queue = [(root, 1)]
        minDep = 0
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth >= minDep and minDep != 0:
                continue
            if node.left is None and node.right is None:
                if minDep > depth or minDep == 0:
                    minDep = depth
            else:
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
        return minDep

    def DFS(self, root):
        stack = [(root, 1)]
        minDep = 0
        while len(stack) > 0:
            node, depth = stack.pop()
            if depth >= minDep and minDep != 0:
                continue
            if node.left is None and node.right is None:
                if minDep > depth or minDep == 0:
                    minDep = depth
            else:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
        return minDep

    def _DFS(self, root, visit, fetchChildren):
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            visit(node)
            for child in fetchChildren(node):
                stack.append(child)

    def visit(Node, ):
        node, depth = Node
        pass

    def fetchChildren(Node, needVisit=None):
        node, depth = Node
        children = []
        if node.left:
            if needVisit is None or needVisit(Node):
                children.append((node.left, depth + 1))
        if node.right:
            if needVisit is None or needVisit(Node):
                children.append((node.right, depth + 1))
        return children

    def getNodeFilter(minDepth=0):
        def needVisit(Node):
            node, depth = Node
            if node is None:
                return False
            if minDepth == 0:
                pass

            # Unfinished ...
        return needVisit


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
print s.minDepth(root)
