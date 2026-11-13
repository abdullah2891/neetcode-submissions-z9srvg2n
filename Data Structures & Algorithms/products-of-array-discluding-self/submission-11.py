class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leading = [nums[0]]
        
        for i in range(1, len(nums)):
            leading.append(leading[i - 1] * nums[i])



        reverse = [nums[-1]]

        for i in range(len(nums) - 2, -1, -1):
            # print(len(nums) ,  i)
            reverse.append(reverse[len(nums) - i - 2] * nums[i])

        reverse = reverse[::-1]
        # print(leading)
        # print(reverse)

        ans = []


        for i in range(0, len(nums)):
            left = leading[i - 1] if i != 0 else 1
            right = reverse[i + 1] if i < len(nums) - 1 else 1

            ans.append(left * right)

        # ans.append(leading[-2])

        return ans