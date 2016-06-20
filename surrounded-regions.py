class Solution(object):
    def __init__(self):
        self.freeStack = []
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        ONE = '1'       # ONE is `free'
        ZERO = 'O'
        X = 'X'

        if len(board) == 0 or len(board[0]) == 0:
            return
        
        self.board = board
        self.HEIGHT = len(board)
        self.WIDTH = len(board[0])

        self.freeStack = []
        
        # mark free '0's to '1's
        ## mark border '0's to '1's, and push to stack
        for i in xrange(self.WIDTH):
            if board[0][i] == ZERO:
                board[0][i] = ONE
                self.freeStack.append((0, i))
            if board[self.HEIGHT - 1][i] == ZERO:
                board[self.HEIGHT - 1][i] = ONE
                self.freeStack.append((self.HEIGHT - 1, i))
        for i in xrange(self.HEIGHT):
            if board[i][0] == ZERO:
                board[i][0] = ONE
                self.freeStack.append((i, 0))
            if board[i][self.WIDTH - 1] == ZERO:
                board[i][self.WIDTH - 1] = ONE
                self.freeStack.append((i, self.WIDTH - 1))
        ## pop and mark neighbors of '1's, and push to stack, util stack is empty
        while len(self.freeStack) > 0:
            newfrees = self._markNeighbors(self.freeStack.pop(), ZERO, ONE)
            self.freeStack.extend(newfrees)
        # flip '0's to 'X's
        for i in xrange(self.HEIGHT):
            for j in xrange(self.WIDTH):
                if board[i][j] == ZERO:
                    board[i][j] = X
        # revert '1's to '0's
        for i in xrange(self.HEIGHT):
            for j in xrange(self.WIDTH):
                if board[i][j] == ONE:
                    board[i][j] = ZERO

    def _markNeighbors(self, position, target, value):
        x, y = position
        points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),]
        valid = []
        for p in points:
            if self._mark(p, target, value):
                valid.append(p)
        return valid

    def _mark(self, position, target, value):
        x, y = position
        if (x >= 0 and x < self.HEIGHT and
            y >= 0 and y < self.WIDTH and
            self.board[x][y] == target
        ):
            self.board[x][y] = value
            return True
        return False


def main():
    m = [
        ['X', 'X', 'X', 'X', 'O',],
        ['X', 'O', 'O', 'X', 'O',],
        ['X', 'X', 'O', 'X', 'O',],
        ['X', 'O', 'X', 'X', 'O',],
    ]
    print m
    s = Solution()
    s.solve(m)
    print m

if __name__ == '__main__':
   main()
