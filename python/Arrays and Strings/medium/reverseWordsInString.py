#-------------------------------------
#two index problem, 
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
	word.append(string[startWordidx:])
	reverseList(word)
    return "".join(word)

def reverseList(list):
	start,end=0,len(list)-1
	while start<end:
		list[start],list[end]=list[end],list[start]
		start+=1
		end-=1




