def reverseString(s):
    temp=s.split()
    print(temp)
    left, right = 0, len(s) - 1

    while left < right:
        # Swap the characters at left and right pointers
        s[left], s[right] = s[right], s[left]

        # Move the pointers towards the center of the string
        left += 1
        right -= 1

    return s
s='hello'
#s = ["h", "e", "l", "l", "o"]
result = reverseString(s)
print(result)  # Output: ["o", "l", "l", "e", "h"]

