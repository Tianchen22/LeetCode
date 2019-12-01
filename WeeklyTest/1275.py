"""
1275. Find Winner on a Tic Tac Toe Game

https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Simple Simulation Question
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        curr, a = 0,[[-1 for i in range(3)]for j in range(3)]
        for move in moves:
            x,y = move[0],move[1]
            a[x][y] = curr
            if (a[x][0] == a[x][1] == a[x][2] == curr
               or a[0][y] == a[1][y] == a[2][y] == curr
               or x == y and a[0][0] == a[1][1] == a[2][2] == curr
               or x + y == 2 and a[0][2] == a[1][1] == a[2][0] == curr):
                return "A" if curr == 0 else "B"
            curr ^= 1
        return "Draw" if len(moves) == 9 else "Pending" 
    
