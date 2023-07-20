from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result={}
        for num in arr:
            result[num]=result.get(num,0)+1

        occurences=[]
        for v in result.values():
            occurences.append(v)

        if len(occurences)==len(set(occurences)):
            return True
        else:
            False

sol=Solution()
print(sol.uniqueOccurrences([1,2,2,1,1,3]))