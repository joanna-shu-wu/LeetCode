from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            print(start)
            print(end)
            lastEnd = output[-1][1]
            print(f'this is last end {lastEnd}' )

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


sol=Solution()
result=sol.merge([[1,3],[2,6],[8,10],[15,18]])
print(result)
