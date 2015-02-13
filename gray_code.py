class Solution:
    # @return a list of integers
    def _grayCode(self, n):
        grayCode = [0]
        grayCodeSet = set(grayCode)
        num = -1
        while num != grayCode[-1]:
            num = grayCode[-1]
            for i in range(n):  # XXX
                s = 1 << i
                new = num ^ s
                if new not in grayCodeSet:  # XX
                    grayCode.append(new)
                    grayCodeSet.add(new)
                    break
                # print 'collide: 0x%x  %d' % (new, n)
        return grayCode

    def grayCode(self, n):
        return map(lambda x: (x>>1) ^ x, range(2 ** n))

    # 00   00   00   00
    # 00   01   01   01
    # 00   00   01   11
    # 00   00   00   10
    #      1    2    3
    # 1. init, 2. mirror, 3. add bit '1' to head
    def ____grayCode(self, n):
        if n < 0:
            return None
        cur = [0] * 2**n
        for width in range(n):
            length = 2 ** width
            head = 1 << width
            for i in range(length):
                cur[2 * length - 1 - i] = cur[i] | head
        return cur


    def ___grayCode(self, n):
        if n < 0:
            return None
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        # grayCode = []
        # XXX first init all list space?
        cur = [0, 1]
        for i in range(1, n):
            nxt = cur[:]
            for d in cur[::-1]:
                nxt.append(d | 1<<i)
            cur = nxt
        return cur

    def __grayCode(self, n):
        if n < 0:
            return None
        if n == 0:
            return [0]
        solved = [None] * (n + 1)
        solved[1] = [0, 1]
        return self.helper(n, solved)

    def helper(self, n, solved):
        if solved[n]:
            return solved[n]
        headLen = n / 2
        tailLen = n - headLen
        head = self.helper(headLen, solved)  # XXX binary divide?
        tail = self.helper(tailLen, solved)
        grayCode = []
        reverse = False
        for t in tail:
            if not reverse:
                for h in head:
                    grayCode.append((h<<tailLen) | t)
            else:
                for h in head[::-1]:
                    grayCode.append((h<<tailLen) | t)
            reverse = not reverse
        solved[n] = grayCode
        return grayCode


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def _test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual([0, 1, 3, 2], self.s.grayCode(2))
        n = 3
        for n in range(100):
            grayCode = self.s.grayCode(n)
            for i in range(n):
                self.assertTrue(i in grayCode)

    def test_small_case(self):
        for i in range(4):
            code = self.s.grayCode(i)
            print i, code, '========='

    def _test_large_case(self):
        for i in range(1000):
        # for i in range(1000, 2000):
            code = self.s.grayCode(i)
            print i, len(code)

if __name__ == '__main__':
    unittest.main()
