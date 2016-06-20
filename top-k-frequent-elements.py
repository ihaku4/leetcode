class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countMap = {}
        for n in nums:
            if countMap.has_key(n):
                countMap[n] += 1
            else:
                countMap[n] = 1
        countList = []
        for key in countMap.keys():
            countList.append((key, countMap[key]))
        countListSorted = sorted(countList, cmp=lambda x,y: cmp(x[1], y[1]), reverse=True)
        returnList = []
        for i in xrange(k):
            returnList.append(countListSorted[i][0])
        return returnList
            
def main():
    s = Solution()
    print s.topKFrequent([1, 1, 1, 8, 9, 9], 2)
    
if __name__ == '__main__':
   main()
