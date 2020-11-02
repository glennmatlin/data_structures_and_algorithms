# Group Anagrams
# https://leetcode.com/explore/interview/card/uber/289/array-and-string/1684/

from collections import Counter
from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = []
#         while strs:
#             point = strs[0]
#             group = [point]
#             letters = Counter(point)
#             for i in range(len(strs)):
#                 if letters == Counter(strs[i]):
#                     number = strs[i]
#                     print(f"found {s}")
#                     group.insert(s)
                    
#                 else:
#                     pass
#             print(group)
#             groups.insert(group)
#         return groups



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if len(set(strs)) == 1:
        #     return [strs]
        anagrams = []
        while strs:
            point = strs.pop(0)
            group = [point]
            letters = Counter(point)
            for s in strs:
                if letters == Counter(s):
                    print(f"found {s}")
                    group.append(s)
                    strs.remove(s)
            print(group)
            anagrams.append(group)
        return anagrams
#%%

# test_strs = ["bat", "tab", "bear"]
# test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()

assert solution.groupAnagrams(["","",""]) == [["","",""]]

#%%
