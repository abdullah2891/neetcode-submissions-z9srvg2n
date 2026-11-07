from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = Counter(s)

        # print(counter)


        for target in t:
            if target in counter:
                counter[target] -= 1 

                if counter[target] == 0:
                    del counter[target]


            
        
        return not bool(counter)