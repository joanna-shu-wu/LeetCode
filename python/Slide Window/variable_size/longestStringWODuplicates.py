'''
slide window recipe: for+if/while
'''
def longestStringWODuplicates(s):
    charSet=set() #initial temp container
    l=0 # initial the beginning of the window,
    res=0 #initial result

    for r in range(len(s)): #update the pointer to a new location
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res=max(res,r-l+1)

    return res

def main():
    print(longestStringWODuplicates('abba'))

if __name__=='__main__':
    main()