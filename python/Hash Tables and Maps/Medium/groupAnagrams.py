'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''


# Time complexity: O(N*M*Log(M))
#N: the length of the input array, M: the length of biggest string in the array
# M*Log(M) is because we sort each string when we pass over it in the loop
# Space complexity: O(N) because we use hashmap to store the data


class Solution:

    def findHash(self,s):
        return ''.join(sorted(s))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anwsers=[]
        m={}

        for s in strs: 
            hashed=self.findHash(s) #find the sorted version of current string. The sorted string called 'hashed' will be the key of the hashmap
            if(hashed not in m):
               m[hashed]=[]
            m[hashed].append(s) # if this is the first time we have the value in the map, we append it to the array that correspond to the hash
        for p in m.values():  #loop over our map values, append current array to our answer
            anwsers.append(p)  #Append the current string to the key(sorted version string)

        return anwsers
      

      