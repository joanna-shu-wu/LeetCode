'''
https://www.youtube.com/watch?v=Y0lT9Fck7qI

Bottom up approach

If you need to climb 5 stairs, how many distinct approach are there?

'''

def climbStair(n):
    one,two=1,1

    for i in range(n-1):
        temp=one
        one=one+two
        two=temp
        
