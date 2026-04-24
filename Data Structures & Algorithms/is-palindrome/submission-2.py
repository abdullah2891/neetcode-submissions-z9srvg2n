class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ''.join([chr.lower() 
            for chr in s.replace(' ', '') 
            if chr.isalpha() or chr.isdigit()])

        return formatted == formatted[::-1]