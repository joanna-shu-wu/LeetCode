'''
Give 1234 and return 4321
'''
import math
def reverse_number(n):
   digit=math.floor(math.log10(n))+1
   return helper(n,digit)  
  
def helper(n,digit):
 if math.floor(n%10)==0:
        return n
 rem=math.floor(n%10)
 return rem*10**(digit-1)+helper(math.floor(n)/10,digit-1)
    

result=reverse_number(1234)
print(result)