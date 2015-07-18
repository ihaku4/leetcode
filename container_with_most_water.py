class Solution:

    def volumn(self, h, t, height):
        return (t - h) * min(height[h], height[t])

    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        h, t = 0, len(height) - 1
        maxVolumn = self.volumn(h, t, height)
        while h < t:
            if height[h] < height[t]:
                cur = h
                while h < t and height[cur] >= height[h]:
                    h += 1
            elif height[h] > height[t]:
                cur = t
                while h < t and height[cur] >= height[t]:
                    t -= 1
            else:
                cur = h
                while h < t and height[cur] >= height[h]:
                    h += 1
                cur = t
                while h < t and height[cur] >= height[t]:
                    t -= 1
            maxVolumn = max(maxVolumn, self.volumn(h, t, height))
        return maxVolumn


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(1, self.s.maxArea([1, 2]))

if __name__ == '__main__':
    unittest.main()
