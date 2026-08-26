class Solution:
    def isValid(self, s: str) -> bool:
        close=set()
        close.add(']')
        close.add('}')
        close.add(')')
        stack=[]
        for i in range(len(s)):
            if s[i] in close:
                if not stack: return False
                if s[i]==')' and stack.pop()!='(': return False
                if s[i]=='}' and stack.pop()!='{': return False
                if s[i]==']' and stack.pop()!='[': return False
            else: stack.append(s[i])
        if not stack: return True
        return False