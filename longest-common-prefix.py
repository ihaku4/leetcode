class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_len = len(strs[0])
        # TODO sort and binary search
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        i = 0
        while i < min_len:
            if not self.isSame(strs, i):
                break
            i += 1
        return strs[0][0:i]

    def isSame(self, strs, i):
        j = 1
        while j < len(strs):
            if strs[j-1][i] != strs[j][i]:
                return False
            j += 1
        return True


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        return

    def test_normal(self):
        self.assertEqual(0, 0)
        self.assertTrue(True)
        self.assertEqual('123', self.s.longestCommonPrefix(['1231',
                                                            '1232',
                                                            '1233',
                                                            '1234',
                                                            '1235', ]))
        self.assertEqual('',
                         self.s.longestCommonPrefix(['2231',
                                                     '1232',
                                                     '1233',
                                                     '1234',
                                                     '1235', ]))
        self.assertEqual('12',
                         self.s.longestCommonPrefix(['12x1',
                                                     '1232',
                                                     '1233',
                                                     '1234',
                                                     '1235', ]))
        self.assertEqual('c',
                         self.s.longestCommonPrefix(['c',
                                                     'c', ]))

if __name__ == '__main__':
    unittest.main()
