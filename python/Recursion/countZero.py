'''Given a number, check if there's any zero'''
'''hint:check remainder'''
'''If remainder equal to 0, increase the count and reduce the number by dividing it by 10'''
import math

# Method 1: put the count inside the argument
def countZero(number):
    count=0
    return helper(number,count)

def helper(number,count):
    if math.floor(number)==0:
        return count

    rem=number%10
    if math.floor(rem)==0:
        return helper(number/10,count+1)
    return helper(number/10,count)

print(countZero(332))