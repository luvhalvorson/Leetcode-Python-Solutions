class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in "{[(":
                st.append(c)
            else:
                
                if st:
                    b = st.pop()
                else:
                    return False
               
                

                if c is "}" and b is not "{":
                    return False
                if c is "]" and b is not "[":
                    return False
                if c is ")" and b is not "(":
                    return False
            
        return True if not st else False