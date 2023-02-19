'''
Give 1234 and return 4321
'''
import math
sum=0
def reverse_number(n):
    global sum
    if math.floor(n)==0:
        return n
    
    rem=math.floor(n%10)
    sum=sum*10+rem
    reverse_number(n/10)
   
    
reverse_number(1234)
print(sum)