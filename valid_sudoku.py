class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # horizontals = [[False] * 9] * 9
        # verticals = [[False] * 9] * 9
        # squares = [[False] * 9] * 9
        horizontals = [[False for x in range(9)] for x in range(9)]
        verticals = [[False for x in range(9)] for x in range(9)]
        squares = [[False for x in range(9)] for x in range(9)]
        row = 0
        while row < len(board):
            col = 0
            while col < len(board[row]):
                num = board[row][col]
                if num != '.':
                    # TODO num need ord(num)??
                    if isinstance(num, str):
                        num = ord(num) - ord('0')
                    num -= 1
                    if horizontals[row][num]:
                        return False
                    if verticals[col][num]:
                        return False
                    squareIndex= (row / 3) * 3 + col / 3
                    if squares[squareIndex][num]:
                        return False

                    horizontals[row][num] = True
                    verticals[col][num] = True
                    squares[squareIndex][num] = True
                col += 1
            row += 1
        return True

    def printSquare(self, square):
        s = ''
        for line in square:
            for c in line:
                s += str(c)
                s += ', '
            s += '\n'
        print s


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.board = [
            '53..7....',
            '6..195...',
            '.98....6.',
            '8...6...3',
            '4..8.3..1',
            '7...2...6',
            '.6....28.',
            '...419..5',
            '....8..79',
            ]
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(True, self.s.isValidSudoku(self.board))

    def _test_2D_array(self):
        # sq = [[1] * 9] * 9
        sq = [[1 for x in range(9)] for x in range(9)]
        self.s.printSquare(sq)
        sq[1][2] = 0
        print sq[1][2]
        self.s.printSquare(sq)

if __name__ == '__main__':
    unittest.main()
