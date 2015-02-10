class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        vote = num[0]
        count = 1
        size = len(num)
        for i in range(1, size):
            if count == 0:
                vote = num[i]
                count += 1
            elif vote == num[i]:
                count += 1
            else:
                count -= 1
        return vote

s = Solution()
print s.majorityElement([1, 2, 3, 1, 1])
print s.majorityElement([1, 2, 3, 2, 1, 3])
print s.majorityElement([1])
print s.majorityElement([2, 2])
num = [1, 2, 1, 2, 1]
print sorted(num)[len(num)/2]
