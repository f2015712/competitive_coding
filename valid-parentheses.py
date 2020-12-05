class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in range(len(s)):
            if s[i] in ['(','[','{'] or len(stack)==0:
                stack.append(s[i])
            else:
                if s[i]==')' and stack[-1]=='(':
                    stack.pop()
                elif s[i]==']' and stack[-1]=='[':
                    stack.pop()
                elif s[i]=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append(s[i])
        #print(len(stack))
        if len(stack)==0:
            return True
        return False
        