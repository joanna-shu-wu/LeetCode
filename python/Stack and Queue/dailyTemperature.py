from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        nextWarmerIndex=0
        result=[0]*len(T)

        for idx in range(len(T)):
            while nextWarmerIndex<len(T):
                if T[idx]<T[nextWarmerIndex]:
                    daysSince=0
                    daysSince+=1
                    result[idx]=daysSince
                    break
                nextWarmerIndex+=1
        return result


#sol=Solution()
#result=sol.dailyTemperatures([73,74,75,71,69,72,76,73])
#print(result)


def dailyTemperatures(T):
    result = [0] * len(T)
    
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            if T[j] > T[i]:
                result[i] = j - i
                break
    
    return result


print(dailyTemperatures([73,74,75,71,69,72,76,73]))