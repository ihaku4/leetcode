class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        numMap = {}
        for i, n in enumerate(nums):
            if numMap.has_key(target - n):
                return numMap[target - n] + 1, i + 1
            numMap[n] = i


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual((1, 2), self.s.twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    unittest.main()
