from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            values_of_dictionary=res[tuple(count)]
            res[tuple(count)].append(s)
        return res.values()

solution=Solution()

print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))