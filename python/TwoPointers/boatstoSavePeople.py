from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # sort in an ascending order
        left =0 # Use two pointers method
        right = len(people)-1
        boats_number =0
        
        
        while(left <=right):
        
            if(left ==right): # two pointers are pointing at the same person
                boats_number+=1
                break
            
            if(people[left]+people[right]<=limit): # If the sum of the lighest and heaviest people are less than the limit, two people can go on a boat. 
                left += 1

            
            right -= 1   # If the heaviest person exceeds the limit, only one person go on a boat 
            boats_number+=1
            
            
            '''if(people[right]>=limit): 
                right -= 1 
                boats_number+=1 ''' # Using the third if statement would slow down the calculation. Since the second and third condition both need to decrement 1 and add one boat, they can be combined as above
            
            
        
        
        
        return boats_number
        