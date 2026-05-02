class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_num = [nums[0]]
        len_nums = len(nums)

        for index in range(1, len_nums):
            prefix_num.append(prefix_num[index-1]* nums[index])


        print(prefix_num)

        suffix_num = [nums[-1]]

        for index in range(len_nums - 1, 0, -1):
            suffix_num.append(suffix_num[len_nums - index - 1] * nums[index - 1])

        reversed = suffix_num[::-1]
        print(reversed)

        ans = [reversed[1]]

        for index in range(1, len(reversed)-1):
            ans.append(prefix_num[index-1] * reversed[index + 1])

        ans.append(prefix_num[-2])


        return ans

