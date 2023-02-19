def stringSkipAHelper(originalString):
    newString=''
    return helper(originalString,newString)

def helper(originalString,newString):
    if len(originalString)==0:
        return newString
    
    currChar=originalString[0]
    if currChar=='a':
        return helper(originalString[1:],newString)
    else:
        return helper(originalString[1:],newString+currChar)

print(stringSkipAHelper('baccaaad'))