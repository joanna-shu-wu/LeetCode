# Dynamic Programming




def numberOfWaysToMakeChange(n, denoms):
   ways=[0 for target_amount in range(n+1)]
   ways[0]=1 #there's only one way to make 0 change which is not do anything.
   for denom in denoms:
       for target_amount in range(1,n+1):
           if denom<=target_amount:
               ways[target_amount]+=ways[target_amount-denom] #just have to know this, tricky
    return ways[n]