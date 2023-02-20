def containsDuplicate(arry):
    hashset = set()
    for n in arry:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(containsDuplicate([3,5,2,2,3]))