class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 0:
            return 0
        if n < 2:
            return 1
        n1, n2 = 1, 1
        i = 2
        while i <= n:
            n1Bak = n1
            n1 = n2
            n2 += n1Bak
            i += 1
        return n2

    def fib(self, n):
        if n < 0:
            return 0
        num, next = 1, 1
        for i in range(n):
            num, next = next, num + next
        return num

    def _climbStairs(self, n):
        solved = [0] * (n + 1)
        solved[0] = 1
        return self.climbStairsRec(n, solved)

    def climbStairsRec(self, n, solved):
        if n < 0:
            return 0
        if solved[n] > 0:
            return solved[n]
        re = self.climbStairsRec(n - 1, solved) + self.climbStairsRec(n - 2, solved)
        solved[n] = re
        return re



import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        print self.s.climbStairs(1)
        print self.s.climbStairs(2)
        for i in range(100):
            print i, self.s.climbStairs(i)
            print i, self.s.fib(i)

if __name__ == '__main__':
    unittest.main()
