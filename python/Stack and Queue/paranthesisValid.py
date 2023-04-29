def isValid(s):
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        print(c)
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack

def main():
    print(isValid("[]"))
   
#[3,2,12,6], 

if __name__=='__main__':
    main()