# Method 1: recursion
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_memo(n, memo):
    if memo is not None:
        return memo[n]
    if n==1 or n==2:
        return 1    
    else:
        return fib(n-1,memo)+fib(n-2,memo)
    memo[n]=fib(n-1)+fib(n-2)
