"""
5297. Jump Game III

https://leetcode.com/problems/jump-game-iii/

BFS + Simulation
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = [start]
        used = [False for x in arr]
        used[start] = True
        while len(q) > 0:
            curr = q[0]
            if arr[curr] == 0:
                return True
            for x in [curr + arr[curr],curr - arr[curr]]:
                if x >= 0 and x < len(arr) and not used[x]:
                    used[x] = True
                    q.append(x)
            q.pop(0)
        return False
        