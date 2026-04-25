class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        len_nums = len(nums)

        for n in range(1, len_nums):
            prefix.append(prefix[n-1] * nums[n])

        post_fix = [nums[-1]]

        for index in range(len_nums - 2, -1, -1):
            post_fix.append(post_fix[len_nums - index - 2] * nums[index])

        post_fix = post_fix[::-1]
        post_fix.append(1) # buffer 1 

        print(prefix)
        print(post_fix)

        ans = [post_fix[1]]

        for index in range(1, len_nums):
            ans.append(prefix[index -1] * post_fix[index + 1])

        
        return ans


        
