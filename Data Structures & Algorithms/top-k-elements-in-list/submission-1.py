import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        heapq.heapify(heap)

        for elem in counter:
            heapq.heappush(heap, (-counter[elem], elem))

        # from pprint import pprint
        # pprint(heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans

        