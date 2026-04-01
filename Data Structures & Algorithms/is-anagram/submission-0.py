from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        s_counter  = Counter(s)

        for string in t:
            if string not in s_counter:
                return False

            s_counter[string] -= 1 

            if s_counter[string] == 0:
                del s_counter[string]


            

        return not bool(s_counter) 