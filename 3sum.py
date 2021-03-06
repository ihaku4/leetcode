class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        num.sort()
        res = []
        for ic, c in ((i, num[i]) for i in xrange(len(num)-1, -1, -1) if num[i] >= 0):
            if ic < len(num) - 1 and c == num[ic + 1]:
                continue
            ib_pre = ic
            for ia, a in ((i, num[i]) for i in xrange(ic) if num[i] <= 0 and num[i] >= -2 * c):
                # -2c < a < -c
                # -c < a
                try:
                    ib = num.index(-a-c, ia + 1, ib_pre)
                    ib_pre = ib
                    triplet = [a, num[ib], c]
                    res.append(triplet)
                except ValueError:
                    continue
        return res

    def _threeSum(self, num):
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
