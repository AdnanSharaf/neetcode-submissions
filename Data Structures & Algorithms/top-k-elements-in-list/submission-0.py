from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        element = Counter(nums)
        heap = []
        for values,freq in element.items():
            heapq.heappush(heap,(freq,values))

            if len(heap)>k:
                heapq.heappop(heap)

        return [ x for freq,x in heap ]

