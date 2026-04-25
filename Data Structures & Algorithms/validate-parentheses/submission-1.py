class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        valid_mapping = {
            ']' : '[',
            ')': '(',
            '}': '{'
        }

        for char in s:
            if char not in valid_mapping: 
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False 

                popped_elemnt = stack.pop()

                if popped_elemnt != valid_mapping[char]:
                    return False


        return len(stack) == 0
            
