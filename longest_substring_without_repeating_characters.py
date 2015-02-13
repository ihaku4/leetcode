class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        lastPosOfChar = [-1] * 256
        currentSubStart = 0
        maxSubLen = 0
        for i, c in enumerate(s):
            #             curSubStart        i, c
            #             |                  |
            # -c----c-----*------------------c-----
            # <--scaned-->*------------------c-----
            if lastPosOfChar[ord(c)] < currentSubStart:
                maxSubLen = max(maxSubLen, i - currentSubStart + 1)
            # -c----c-----*----c-------------c-----
            # -c----c----------c*------------c-----
            else:
                currentSubStart = lastPosOfChar[ord(c)] + 1
            lastPosOfChar[ord(c)] = i
        return maxSubLen


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(3, self.s.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(self.s.lengthOfLongestSubstring('bbbbbbbbb'), 1)
        self.assertEqual(self.s.lengthOfLongestSubstring('123456727abcdefghijklmnm'), 16)

if __name__ == '__main__':
    unittest.main()
