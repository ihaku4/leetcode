# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):

    """Docstring for BinaryTree. """

    def __init__(self, serial='{}'):
        """TODO: to be defined1.

        :serial: TODO

        """
        self._serial = serial

    def deserialize(self, serial=None):
        if serial is None:
            serial = self._serial
        serial = serial.strip()
        if len(serial) < 2:
            return None
        serial = serial[1:-1]
        nodeValues = serial.split(',')
        if len(nodeValues) == 0:
            return None

        root = self.createNode(nodeValues.pop(0))
        nodeQueue = [root]
        while len(nodeValues) >= 2:
            lv = nodeValues.pop(0)
            rv = nodeValues.pop(0)
            node = nodeQueue.pop(0)
            node.left = self.createNode(lv)
            node.right = self.createNode(rv)
            if node.left:
                nodeQueue.append(node.left)
            if node.right:
                nodeQueue.append(node.right)
        return root

    def createNode(self, strV):
        if not strV:
            return None
        strV = strV.strip()
        if strV == '#' or strV == '':
            return None
        return TreeNode(int(strV))
