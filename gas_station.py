class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        need = [0] * len(gas)
        possible = []
        i = 0
        totalBalance = 0
        while i < len(gas):
            need[i] = cost[i] - gas[i]
            totalBalance -= need[i]
            if need[i] <= 0:
                possible.append(i)
            i += 1
        if totalBalance < 0:
            return False
        if len(possible) == len(gas):
            return True
        # if len possible > len impossible XXX
        while len(possible) > 0:
            startPoint = possible.pop()
            if self.travelable(startPoint, need):
                return startPoint
        return -1

    def travelable(self, start, consumptions):
        balance = -consumptions[start]
        i = start + 1 if start + 1 < len(consumptions) else 0
        while i != start:
            balance -= consumptions[i]
            if balance < 0:
                return False
            i = i + 1 if i + 1 < len(consumptions) else 0
        return True
