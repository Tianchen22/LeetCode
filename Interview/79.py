"""
79. Word Search

https://leetcode.com/problems/word-search/

HashMap + BFS
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        d,length = [[1,0],[0,1],[-1,0],[0,-1]], len(word)
        n,m = len(board), len(board[0])
        self.used = {}
        def dfs(x,y,curr):
            self.used[(x,y)] = True
            if self.res == True:
                return
            if curr >= length: 
                self.res = True
                return
            for i in range(4):
                tx,ty = x + d[i][0], y + d[i][1]
                if tx >= 0 and tx < n and ty >= 0 and ty < m and board[tx][ty] == word[curr] and not self.used.get((tx,ty),False):
                    dfs(tx,ty,curr+1)
            self.used[(x,y)] = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and not self.res:
                    dfs(i,j,1)
                    if self.res: return True
        return False
            
            
