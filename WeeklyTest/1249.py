"""
1249 Minimum Remove to Make Valid Parentheses    

Problem link:
  https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
  
Thought:
  Loop twice, one from left to right and one from right to left.
  to check if the brackets are matched, if the bracket is not matched, then ignore it.
"""

  def minRemoveToMakeValid(self, s: str) -> str:        
        count = 0
        res,res2 = [] , []
        for x in s:
            if x != '(' and x !=')':
                res.append(x)
            elif x == '(':
                res.append(x)
                count += 1
            else:
                if count > 0:
                    count -= 1
                    res.append(x)
        count = 0
        for i in range(len(res)-1,-1,-1):
            x = res[i]
            if x != '(' and x !=')':
                res2.append(x)
            elif x == ')':
                res2.append(x)
                count += 1
            else:
                if count > 0:
                    count -= 1
                    res2.append(x)
        return "".join(res2[::-1])
