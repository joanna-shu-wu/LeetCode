# O(n^2) time | O(1) space
def bubbleSort(array):
    isSorted=False
    counter=0
	while not isSorted:
		isSorted=True
		for i in range(len(array)-1-count):
			if array[i]>array[i+1]:
				array[i],array[i+1]=array[i+1],array[i]				
				isSorted=False #reset to False once the code enters the if statement. This will loop through a whole array again. So time complexity is O(n^2)
		counter+=1 #increase by 1 for each for iteration
    return array
