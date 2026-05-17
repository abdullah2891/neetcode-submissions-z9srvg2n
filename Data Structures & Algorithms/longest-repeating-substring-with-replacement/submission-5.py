class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        test input XYYX



        '''
        left = 0
        window = defaultdict(int)
        max_char = 0
        ans = 0


        for right in range(len(s)):
            window[s[right]] +=1 
            max_char = max(max_char, window[s[right]])

            while right - left + 1 - max_char > k:
                window[s[left]] -= 1
                left += 1 

            ans = max(ans, right - left + 1)


        return ans