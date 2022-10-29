#-------------------------------------
#two index problem, 
#O(n) time|O(n) space
#-------------------------------------

def reverseWordsInString(string):
    word=[]
	startWordidx=0
	for idx in range(len(string)): 
		if string[idx]==" ": #idx keeps moving along the array until it find a space
			word.append(string[startWordidx:idx]) #once idx hit a space, we save the word, then we update  the startOfWord to idx
			startWordidx=idx
		elif string[startWordidx]==" ": #if the character is not equal to space, we check if the startOfWord is equal to a space
			word.append(" ")
			startWordidx=idx
	word.append(string[startWordidx:]) # It's for the last word because it would never meet the for loop condition
	reverseList(word)
    return "".join(word)#take all the elements in the list (reversed) and create a string

def reverseList(list):
	start,end=0,len(list)-1
	while start<end:
		list[start],list[end]=list[end],list[start]
		start+=1
		end-=1




