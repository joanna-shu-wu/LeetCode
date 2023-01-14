def mergeSort(array):
    if len(array)==1:
        return array
    mid=round(len(array)/2)
    left_array=mergeSort(array[:mid])
    right_array=mergeSort(array[mid:])
    merge(left_array,right_array)

def merge(array1, array2):
    i=0
    j=0
    k=0
    new_array=[]
    while(i<len(array1) or j<len(array2)):
        if array1[i]<array2[j]:
            new_array[k]=array1[i]
            
            i=+1
            k=+1
        else:
            new_array[k]=array1[j]
            
            j=+1
            k=+1
    
    while(i<len(array1)):
        new_array=array1[i]
        i+=1
        k+=1
    while(j<len(array2)):
        new_array=array1[j]
        j+=1
        k+=1


print(mergeSort([5,4,3,2,1]))