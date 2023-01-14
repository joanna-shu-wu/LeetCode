def patterns(rows):
    columns=0
    return helper(rows,columns)

def helper(rows,columns):
    if columns==rows:
        return 
    if rows>=columns:  
        helper(rows,columns+1)
        print('*'*(rows-columns))


    patterns(4)