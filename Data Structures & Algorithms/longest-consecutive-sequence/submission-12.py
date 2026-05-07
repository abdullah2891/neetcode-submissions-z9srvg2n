class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        ans = 0
        for n in nums:
            # start of pivot number
            if n-1 not in seen:
                streak = n
                while streak in seen:

                    streak += 1

                    ans = max(ans, streak - n)

        return ans
                
