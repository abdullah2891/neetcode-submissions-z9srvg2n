class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)


        for s in strs:
            mask  = [0] * 26
            
            for j in s:
                offset = ord(j) - ord('a')

                mask[offset] += 1

            seen[tuple(mask)].append(s)

        

        return list(seen.values())

