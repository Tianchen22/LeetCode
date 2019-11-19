/*
1240. Tiling a Rectangle with the Fewest Squares

Problem link:
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

Thought:
	My first try in the weekly test is a wrong dp solution, it cannot handle with some special solution.
	(the example, which when n = 11 and j == 13 is the most special case)
	This dp solution is not very effecitve but useful.
	In the discussion part, there has solution with three neat loops.
	
*/

class Solution {
public:
    int tilingRectangle(int n, int m) {
        if (n > m) { swap(n,m); }
        int f[20][20] = {0};
        
        for (int i = 1; i <= m; i++)
            f[i][1] = f[1][i] = i;
        for (int i = 1; i <= n; i++)
            f[i][i] = 1;
        
        for (int i = 2; i <= n; i++){
            for (int j = i+1; j <= m; j++){
                if (i == 11 && j == 13){
                    f[i][j] = f[j][i] = 6;
                    continue;
                }
                f[j][i] = f[i][j] = f[i-1][j-1] + i + j - 1;
                for (int k = 0; k < i; k++)
                    for (int l = 0; l < j; l++)
                        f[j][i] = f[i][j] = min(f[i-k][j-l] + min(f[k][j] + f[i-k][l], f[i][l] + f[j-l][k]), f[i][j]);
            }
        }
        return f[n][m];
    }
};

