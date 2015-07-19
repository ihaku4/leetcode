class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct2(self, nums):
        maxP = None

        i = 0
        while i < len(nums):
            # 1) Ignore 0s
            while i < len(nums) and nums[i] == 0:
                if maxP is None:
                    maxP = 0
                else:
                    maxP = max(maxP, 0)
                i += 1
            if i == len(nums):
                break

            # 2) Multiply util 0. Record head, tail, product
            h = i
            prod = 1
            while i < len(nums) and nums[i] != 0:
                prod *= nums[i]
                i += 1
            t = i - 1
            if maxP is None:
                maxP = prod
            else:
                maxP = max(maxP, prod)

            # 3) Handle negative product
            if prod < 0:
                div = 1
                h0 = h
                while h0 < t and nums[h0] > 0:
                    div *= nums[h0]
                    h0 += 1
                div *= nums[h0]
                if h0 < t:
                    maxP = max(maxP, prod / div)

                div = 1
                t0 = t
                while h < t and nums[t0] > 0:
                    div *= nums[t0]
                    t0 -= 1
                div *= nums[t0]
                if h < t0:
                    maxP = max(maxP, prod / div)
        return maxP

    def maxProduct(self, A):
        minNow = A[0]
        maxNow = A[0]
        output = maxNow
        for num in A[1:]:
            minPrev = minNow
            maxPrev = maxNow
            print minPrev, maxPrev
            minNow = min(num, minPrev * num, maxPrev * num)
            maxNow = max(num, minPrev * num, maxPrev * num)
            output = max(output, maxNow)
        return output

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(6, self.s.maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, self.s.maxProduct([-2, 0, -1]))
        self.assertEqual(6, self.s.maxProduct([2, 3, 0, 0, -2, 4]))
        self.assertEqual(16, self.s.maxProduct([2, 3, 0, 0, -2, 4, 4]))
        print '-------'
        self.assertEqual(16, self.s.maxProduct([2, 3, 0, 0, 4, 4]))

if __name__ == '__main__':
    unittest.main()
