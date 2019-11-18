"""
1247 Minimum Swaps to Make Strings Equal   

Problem link:
  https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
  
Thought:
  count the 'x' and 'y' number. 
  then find the module of x and y,
  the res plus the half of x and y,
  if x and y all left 1, res plus 2,
  if x and y total left 1, then the result is not doable.
"""
  
  def minimumSwap(self, s1: str, s2: str) -> int:
        if (len(s1)!= len(s2)):
            return -1
        countx,county,res = 0,0,0
        
        for i in range(len(s1)):
            if (s1[i] != s2[i]):
                if s1[i] == 'x':
                    countx += 1
                else:
                    county += 1
                
        res += countx // 2
        countx %= 2
        res += county // 2
        county %= 2
        if (countx == 1 and county == 1):
            res += 2
        elif(countx + county == 1):
            return -1
        return res
        
                    
                
