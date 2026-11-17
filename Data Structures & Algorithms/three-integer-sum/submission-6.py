class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        len_nums = len(nums)
        seen = set()
        
        prev = None 
        ans = []

        for i in range(len_nums):
            target = nums[i]
            j =  i + 1 
            k = len(nums) - 1 
            print(target, prev)
            if target == prev:
                continue 

            while j < k:
                # print(nums[i] , nums[j], nums[k])

                sum_val = nums[i] + nums[j] + nums[k]

                seen_tuple = (nums[i], nums[j], nums[k])

                if sum_val == 0 and seen_tuple not in seen:
                    seen.add(seen_tuple)
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    continue

                if sum_val  < 0:
                    j += 1 
                else:
                    k -= 1 
                                

            prev = nums[i]



        return ans 


