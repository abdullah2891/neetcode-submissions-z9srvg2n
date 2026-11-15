import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = nums

        heapq.heapify(heap)

        # print(heap)
        ans = 0
        count = 0
        
        temp = None

        
        while heap:
            elem = heapq.heappop(heap)
            if elem == temp:
                temp = elem
                continue

            # check out sane pattern of counting consequtive stuff 
            if temp is None or elem - temp == 1 or abs(temp - elem)== 1:
                count += 1 

            else:
                count = 1
            
            # print(temp, elem, count)


            temp = elem




            ans = max(ans, count)


        return ans