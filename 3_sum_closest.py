class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()

        minSum = sum(nums[:3])
        for i in xrange(len(nums)):
            h = i + 1
            t = len(nums) - 1
            while h < t:
                currSum = sum((nums[i], nums[h], nums[t]))
                if currSum > target:
                    t -= 1
                elif currSum < target:
                    h += 1
                else:
                    return currSum
                
                if abs(target - currSum) < abs(target - minSum):
                    minSum = currSum

        return minSum


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_default_case(self):
        self.assertEqual(2, Solution().threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(3, Solution().threeSumClosest([0, 1, 2], 3))

if __name__ == '__main__':
    unittest.main()
