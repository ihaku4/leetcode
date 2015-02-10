class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:  # TODO test remove this
            return s
        m = {}
        for i in range(1, nRows + 1):
            m[i] = []
        i = 1
        add = 1
        for c in s:
            m[i].extend(c)  # XXX
            if i == nRows:
                add = -1
            elif i == 1:
                add = 1
            i = i + add
        result = ''
        for i in range(1, nRows + 1):
            result += ''.join(m[i])  # XXX
        return result


import unittest


class Test(unittest.TestCase):

    s = Solution()

    def test_s(self):
        self.assertEqual(Test.s.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        print Test.s.convert("ybgmspclxrseqknqalzuttuhknurlbajeixwxzjxscbkmrapcbjwvffhubyf", 31)

unittest.main()
