"""
1233. Remove Sub-Folders from the Filesystem

Problem link:
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

Thought:
	first sort the list
	then if the folder is the sub folder, the current string will start with 
	the last substring in the result, otherwise current list append to the list.
"""

def removeSubfolders(self, folder: List[str]) -> List[str]:
	folder.sort()
	res = []
	res.append(folder[0])
	for i in range(1,len(folder)):
		if not folder[i].startswith(res[-1] + "/"):
			res.append(folder[i])
	return res
	
