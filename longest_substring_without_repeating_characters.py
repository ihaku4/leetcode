class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        map = {}
        i = 0
        subIndex = 0
        maxLen = 0
        while i < len(s):
            if s[i] not in map or map[s[i]] < subIndex:
                maxLen = max(maxLen, i - subIndex + 1)
            else:
                subIndex = map[s[i]] + 1
            map[s[i]] = i
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
