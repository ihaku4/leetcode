class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if len(num) <= 2:
            return num[0]
        map = {}
        throttle = len(num) / 2 + len(num) % 2
        for n in num:
            if n in map:
                map[n] += 1
                if map[n] == throttle:
                    return n
            else:
                map[n] = 1
        return -1

s = Solution()
print s.majorityElement([1, 2, 3, 1, 1])
print s.majorityElement([1, 2, 3, 2, 1, 3])
print s.majorityElement([1])
print s.majorityElement([2, 2])
