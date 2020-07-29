import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq.keys():
                tmp = freq[nums[i]]
                tmp += 1
                freq[nums[i]] = tmp
            else:
                freq[nums[i]] = 1

        klargestlist = heapq.nlargest(k, freq, key=freq.get)
        return klargestlist
