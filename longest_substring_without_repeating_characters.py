class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        map = {}
        i = 0
        subIndex = 0
        maxLen = 0
        while i < len(s):
            if s[i] not in map:
                if maxLen < i - subIndex + 1:
                    maxLen = i - subIndex + 1
            else:
                lastSubIndex = subIndex
                subIndex = map[s[i]] + 1
                # efficiency improve
                if subIndex - lastSubIndex < i - subIndex:
                    for j in range(lastSubIndex, subIndex):
                        map.pop(s[j])
                else:
                    map = {}
                    for j in range(subIndex, i):
                        map[s[j]] = j

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
