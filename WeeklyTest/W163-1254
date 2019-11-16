Problem link:
  https://leetcode.com/problems/number-of-closed-islands/

Thought:
  The island is closed 0 surrounded by 1 (Careful! The boundary can't be considered as 1)
  just using loops and bfs to change all island 0 to island 1.
  
Solution using Python:
  def closedIsland(self, grid: List[List[int]]) -> int:
      res,n,m = 0,len(grid),len(grid[0])        
      if n < 3 or m < 3:
          return 0

      def bfs(fx,fy):
          a,dx,dy = [[fx,fy]],[1,0,-1,0],[0,1,0,-1]
          le,re = 0,1
          flag = True
          while le < re:
              x,y = a[le][0],a[le][1]
              for i in range(4):
                  tx ,ty = x + dx[i], y + dy[i]
                  if tx < 0 or tx >= n or ty < 0 or ty >= m:
                      flag = False
                      continue;
                  if grid[tx][ty] == 0:
                      grid[tx][ty] = 1
                      a.append([tx,ty])
                      re += 1
              le += 1
          if flag:
              return 1
          else:
              return 0

      for i in range(1,n-1):
          for j in range(1,m-1):
              if grid[i][j] == 0:
                  grid[i][j] = 1
                  res += bfs(i,j)
      return res
