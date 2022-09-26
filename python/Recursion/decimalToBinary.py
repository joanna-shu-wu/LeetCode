def findBinary(num, binary):
    if num==0:
        return binary
    
    binary=str((num%2))+binary
    return findBinary(num//2,binary)



print(findBinary(233," "))


def decimalToBinary(ip_val):
    if ip_val >= 1:
    # recursive function call
        decimalToBinary(ip_val // 2)
    
    # printing remainder from each function call
    print(ip_val % 2, end = '')

decimalToBinary(233)