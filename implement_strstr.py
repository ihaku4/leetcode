class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        matchedPos = {}
        i = 0
        while i < len(haystack):
            unmatched = []
            # TODO first check the smallest in mactchedPos
            matchedPos[i] = True
            for start in matchedPos:
                # XXX if len needle == 0
                if haystack[i] == needle[i - start]:
                    if i - start == len(needle) - 1:
                        return start
                else:
                    unmatched.append(start)
            for u in unmatched:
                matchedPos.pop(u)
            i += 1
        return -1


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(3, self.s.strStr('123456', '456'))
        self.assertEqual(11, self.s.strStr('4545454544445612345666', '456'))
        self.assertEqual(15, self.s.strStr('aaaaaaaaaaaaaaaaabaaaa', 'aab'))
        self.assertEqual(0, self.s.strStr('a', ''))

if __name__ == '__main__':
    unittest.main()
