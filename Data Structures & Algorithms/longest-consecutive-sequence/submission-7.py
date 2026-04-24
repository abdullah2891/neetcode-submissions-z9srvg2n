class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)

        ans = 0

        for n in nums:
            # does it have left neighbor 
            if n -1 not in seen:
                curr = 0 
                while (n  + curr) in seen:
                    curr += 1 

                ans = max(ans, curr)


        return ans