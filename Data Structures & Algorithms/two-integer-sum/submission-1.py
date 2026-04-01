class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index in range(0, len(nums)):
            n = nums[index]

            diff = target - n
            
            if n in seen:
                return [seen[n], index]


            seen[diff] = index

        return []            