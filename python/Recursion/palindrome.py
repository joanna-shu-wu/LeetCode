def isPalindrome(word_string):
    if len(word_string)==0 or word_string==1:
        return True
    if word_string[0]==word_string[len(word_string)-1]: #Add another call in the call stack and shrink the search space, i.e., only look at the substring for the next call stack
        return isPalindrome(word_string[1:len(word_string)-1])
    return False # Passing the True or False in the call stack. You don't have to declare a variable to store it


print(isPalindrome('racecar'))

print(isPalindrome('hello'))