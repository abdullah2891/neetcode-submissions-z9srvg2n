class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        curr_seen = set()
        ans = 0 


        while r < len(s):
            curr_string = s[r]
            if curr_string not in curr_seen:
                curr_seen.add(curr_string)

                ans = max(ans, r -l + 1)
                r +=1 
            else:
                # print(curr_string, s[l])
                curr_seen.remove(s[l])
                l += 1

        return ans