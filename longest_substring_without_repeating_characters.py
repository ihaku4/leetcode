class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        charPos = [-1] * 256
        i = 0
        subIndex = 0
        maxLen = 0
        while i < len(s):
            if charPos[ord(s[i])] < subIndex:
                maxLen = max(maxLen, i - subIndex + 1)
            else:
                subIndex = charPos[ord(s[i])] + 1
            charPos[ord(s[i])] = i
            i += 1
        return maxLen


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
