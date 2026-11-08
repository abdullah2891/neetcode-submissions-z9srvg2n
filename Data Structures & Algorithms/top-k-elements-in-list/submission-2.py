import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = []

        heapq.heapify(freq)

        for key in counter:
            heapq.heappush(freq, (-counter[key], key) )


        ans = []

        # print(freq)

        for _ in range(k):
            top = heapq.heappop(freq)

            ans.append(top[1])


        return ans