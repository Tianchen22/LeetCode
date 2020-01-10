"""
1311. Get Watched Videos by Your Friends

https://leetcode.com/problems/get-watched-videos-by-your-friends/

bfs + set + sort!
*Anyway, learn a brilliant way from the discussion:
https://leetcode.com/problems/get-watched-videos-by-your-friends/discuss/470743/Python-6-lines-bfs-solution
I will put the code down below(Well done)
"""

#first version(basic but clear and readable)
class Solution:
    def watchedVideosByFriends(self, w: List[List[str]], f: List[List[int]], id: int, k: int) -> List[str]:
        q,used,st,res = [id],{},{},[]
        used[id],st[id] = True,0
        while len(q) > 0 and st[q[0]] <= k:
            c = q[0]
            for x in f[c]:
                if not used.get(x,False):
                    used[x],st[x] = True,st[c] + 1
                    if st[x] == k:
                        res[-1:-1] = w[x]
                    q.append(x)
            q.pop(0)
        p = collections.Counter(res)
        return sorted(p.keys(),key = lambda x:(p[x],x))
		
#second version(brilliant, only 8 lines)
class Solution:
    def watchedVideosByFriends(self, w: List[List[str]], f: List[List[int]], id: int, k: int) -> List[str]:
        used,bfs = {id},{id}
        for _ in range(k):
            bfs = {j for i in bfs for j in f[i] if j not in used}
            used |= bfs
        p = collections.Counter([j for i in bfs for j in w[i]])
        return sorted(p.keys(),key = lambda x:(p[x],x))
        