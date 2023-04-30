'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


'''



'''
Example:
Input digit ='23'
ans=[]
index=0
combination=""

currentDigit=digits[0]=2
curString=m[2]=abc
i=0,1,2


'''

class Solution:

    def backtracking(self, ans,m,digits,combination,index): #digits is the input digits, current combination we got so far, the current index that traverse the input digit
        if(index>len(digits)): #sanity check. The index is the current position of the digit. If index is bigger than the length of digit, it's out of bound so we just return the previous recursive
            return
        if(len(combination)==len(digits)): #check if the combiniation string is same as the digit size
            ans.append(combination[:]) #it's valid so push it to the answer array and return the current recursive call
            return
        
        currentDigit=digits[index]
        curString=m[currentDigit]

        for i in range(len(curString)): #loop over the curString. 
            self.backtracking(ans,m,digits,combination+curString[i], index+1) # in the loop, call the backtracking function but add 1 to the index and add the curString to the combination

    def letterCombinations(self, digits: str) -> List[str]:
        ans=[] #it contains the final answer
        if(len(digits)==0): #check if the input digit is valid. If it's empty, just return it without going further
            return ans 
        
        m={} #maps the digit to the string

        m['2']='abc'
        m['3']='def'
        m['4']='ghi'
        m['5']='jkl'
        m['6']='mno'
        m['7']='pqrs'
        m['8']='tuv'
        m['9']='wxyz'


        self.backtracking(ans,m,digits,"",0)

        return ans
    



