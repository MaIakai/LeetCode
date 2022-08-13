class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left=['(','{','[']


        answer=True
        for char in s:
            if char in left:
                stack.append(char)
                
            top=None
            # print("top:",top)
            # print("stack:",stack)
            # print("char=:", char)
            if stack==[]:
                answer=True
            else:
                top=stack[-1]
            if char == ')' :
                if top != '(':
                    answer=False
                    break
                else:
                    stack.pop()
            if char=='}':
                if top !='{':
                    answer=False
                    break
                else:
                    stack.pop()

            if char==']' :
                if top !='[':
                    answer=False
                    break
                else:
                    stack.pop()
        
        if stack!=[]:
            return False
        return answer




