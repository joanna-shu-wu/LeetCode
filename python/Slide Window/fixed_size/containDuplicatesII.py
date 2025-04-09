from typing import List
#Joanna's style
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in numSet:
                return True
            
            numSet.add(nums[r])

            if r - l >= k:
                numSet.remove(nums[l])
                l += 1
        
        return False

#chatGPT style
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])

        # Maintain window size k
        if len(seen) > k:
            seen.remove(nums[i - k])

    return False
