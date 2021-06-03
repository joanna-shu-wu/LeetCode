'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# Use the sliding window technique
# 1. Init two pointers both at 0. They will eventually contain the start and end position of the answer substring
# 2. Create an empty map which have a key-value pair <char, position>
# 3. Loop through the input string as long as left and right pointer are smaller than the length of the input string. 
# 4. Within the loop, save the value of right pointer to variable called 'el'. And use if statement to check the char pointed by the right pointer exist in the map
# 5. If the char pointed by right pointer exist in the map, set left pointer to the position of the next start: max(l+map[el]+1) 
# 6. After the if statement, set m[el] to right
# 7. Use max function to check the current window has a bigger length than the previous one
# 8. Move the right pointer a step to the right

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        left =0
        right =0
        ans =0
        n=len(s)
        while(left<n and right<n):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right # step 6: Save the elemetn and its position to the map
            ans = max(ans,right-left+1)
            right+=1
        return ans