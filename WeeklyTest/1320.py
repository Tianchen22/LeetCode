"""
1320. Minimum Distance to Type a Word Using Two Fingers

https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

Hard!!!!
Using loops + dfs is very difficult to solve depend on 
the complicated possibilty that may occur

Using Top-Down DP to solve the different situations -> dp[position1,position2]
Again, Hard!!

The details are shown in lee's discussion, link below
https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/discuss/477652/JavaC%2B%2BPython-DP-Solution-O(1)-Space
"""
class Solution:
    def minimumDistance(self, a: str) -> int:
        def dis(a,b):
            return 0 if a == -1 else abs(a // 6 - b // 6) + abs(a % 6 - b % 6) 
        n, dp, dp2, MAX_INT = len(a), {( -1, ord(a[0]) - 65) : 0}, {}, 5000
        for c in [ord(c) - 65 for c in a[1:]]:
            for a,b in dp:
                dp2[a,c] = min(dp2.get((a,c),MAX_INT), dp[a,b] + dis(b,c))
                dp2[c,b] = min(dp2.get((c,b),MAX_INT), dp[a,b] + dis(a,c))
            dp,dp2 = dp2,{}
        return min(dp.values())