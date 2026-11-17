class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        len_nums = len(nums)
        # seen = set()
        
        ans = []

        for i in range(len_nums):
            target = nums[i]
            j =  i + 1 
            k = len(nums) - 1 
            # print(target, prev)
            if i > 0 and target == nums[i -1 ]:
                continue

            while j < k:
                # print(nums[i] , nums[j], nums[k])

                sum_val = nums[i] + nums[j] + nums[k]

                # seen_tuple = (nums[i], nums[j], nums[k])

                if sum_val == 0:
                    # seen.add(seen_tuple)
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1 
                    k -= 1 

                    while j < k and nums[j] == nums[j -1] :
                        j += 1 

                    continue

                if sum_val  < 0:
                    j += 1 
                else:
                    k -= 1 
                                



        return ans 


