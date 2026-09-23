from collections import defaultdict
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        res = defaultdict(int)
        result = []
        final = []

        for i in range(len(nums)):
            res[nums[i]] += 1
        for key , value in res.items() :
            result.append((value,key))

        # print(result)

        result.sort(reverse= True)

        for i in range(k):
            final.append(result[i][1])
        # print(final)

        return final
        """

        cnt = Counter(nums)

        heap = []

        for key,value in cnt.items() :
            heapq.heappush(heap,(value,key))
            if len(heap) > k :
                heapq.heappop(heap)
        return [num for value,num in heap]
        
        """

        freq = Counter(nums)

        heap = []

        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
        
        return [num for count,num in heapq.nlargest(k,heap)]
        """