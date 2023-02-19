def stringSkipA(string):
    if len(string)==0:
        return ' '
    
    idx=0
    currentString=string[idx]
    if currentString=='a':
        return stringSkipA(string[1:])
    else:
        return currentString+stringSkipA(string[1:])


print(stringSkipA('baccaaad'))
