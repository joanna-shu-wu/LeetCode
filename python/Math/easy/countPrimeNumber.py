'''

Count the number of prime numbers less than a non-negative number, n.

'''

# Sieve of Eratosthenes
# 1. Define a boolean array of size n and set all elemetns to True except 0 and 1. Assume every elements in the array are prime
# 2. Loop the number from 2 until sqrt(N)
# 3. Using if statement to change the elements i the array from prime to non-prime if the element is the multiple of the number


class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<2): # if the array is 1 or 0,1. There is no prime numner
            return 0
        isPrime = [True] *n # Assume every elements from 2 to n in the array are prime numbers
        isPrime[0] = isPrime[1] = False 

        for i in range(2,int(math.ceil(math.sqrt(n)))): # Sieve of Eratosthenes says we just need to loop until the square root of n 
            if(isPrime[i]):
                for multi_i in range(i*i,n,i): 
                    isPrime[multi_i] = False # all the i that has multiple are not prime number
        return sum(isPrime)