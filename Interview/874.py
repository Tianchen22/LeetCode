"""
874. Walking Robot Simulation

https://leetcode.com/problems/walking-robot-simulation/

Use Dic{} to check if the current point is obstacle
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d, dire, res, check = [[0,1],[1,0],[0,-1],[-1,0]], 0 , 0, {}
        for x in obstacles:
            check[(x[0],x[1])] = False
        x,y = 0,0
        for k in commands:
            if k == -1:
                dire = 0 if dire == 3 else dire + 1
            elif k == -2:
                dire = 3 if dire == 0 else dire - 1
            else:
                for i in range(k):
                    dx,dy = x+d[dire][0], y+d[dire][1]
                    if check.get((dx,dy),True):
                        x,y = dx,dy
                    else:
                        break      
            res = max(res,x*x+y*y)
        return res
