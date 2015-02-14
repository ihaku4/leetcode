class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        # res = []  # TODO use set instead of list ?
        res = {}
        for ia, a in enumerate(num):
            for ib, b in ((x, num[x]) for x in xrange(ia + 1, len(num))):
                for ic, c in ((x, num[x]) for x in xrange(ib + 1, len(num))):
                    triplet = [a, b, c]
                    if sum(triplet) == 0 and tuple(triplet) not in res:
                        res[tuple(triplet)] = triplet
        return res.values()

arr = [-1, 0, 1, 2, -1, -4]
s = Solution()
print s.threeSum(arr)
