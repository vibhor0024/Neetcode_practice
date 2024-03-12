class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        i = 0
        
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



