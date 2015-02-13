# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = [node]
        oldMap = {node.label: node}
        newMap = {}
        visit = 0
        # clone nodes without real neighbor relations
        while visit < len(queue):
            cur = queue[visit]

            # create new and clone label
            newNode = UndirectedGraphNode(cur.label)
            # temperately link new node's neighbors to old
            newNode.neighbors = cur.neighbors
            newMap[newNode.label] = newNode

            # iterate neighbors and check if not in map
            for n in cur.neighbors:
                if n.label not in oldMap:
                    # push new 'old node' in neighbors to queue
                    queue.append(n)
                    # add neighbors to map
                    oldMap[n.label] = n

            visit += 1

        # connect new node's neighbors to true neighbors
        for label in newMap:
            newNode = newMap[label]
            newNeighbors = []
            for neighbor in newNode.neighbors:
                newNeighbors.append(newMap[neighbor.label])
            newNode.neighbors = newNeighbors

        return newMap[node.label]
