class Solution:
    delimeter = 'é'
    def encode(self, strs: List[str]) -> str:
        ans = ""


        for s in strs:
            length_string = str(len(s) + 1)  

            ans += length_string + "_"+ s + '#'


        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0


        while index < len(s):
            freq = ''
            while s[index] < '_':
                freq += s[index]
                index += 1

            
            
            count = int(freq)

            # print(count)
            j = 2
            temp = ''

            while j <= count:
                temp += s[index + j - 1]

                j += 1 

            ans.append(temp)
            # print(ans)

            index += j 


        return ans
    