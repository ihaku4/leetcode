class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum2(self, nums, target):
        numsWithIndex = []
        for i, n in enumerate(nums):
            numsWithIndex.append((i + 1, n))
        numsWithIndex.sort(cmp=lambda x, y: x[1] - y[1])

        head, tail = 0, len(numsWithIndex) - 1
        while head < tail:
            if numsWithIndex[head][1] + numsWithIndex[tail][1] > target:
                tail -= 1
            elif numsWithIndex[head][1] + numsWithIndex[tail][1] < target:
                head += 1
            else:
                return (min(numsWithIndex[head][0], numsWithIndex[tail][0]),
                        max(numsWithIndex[head][0], numsWithIndex[tail][0]))
        return None

    def twoSum(self, nums, target):
        numMap = {}
        for i, n in enumerate(nums):
            numMap[n] = i
        for i, n in enumerate(nums):
            #if target - n in numMap.keys():
            if numMap.has_key(target - n) and numMap[target - n] != i:
                return i + 1, numMap[target - n] + 1


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual((1, 2), self.s.twoSum([2, 7, 11, 15], 9))

if __name__ == '__main__':
    unittest.main()
