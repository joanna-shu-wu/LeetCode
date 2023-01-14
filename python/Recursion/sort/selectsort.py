def selectsort(numbers,current_pos,last_position,max):
    #current_pos=columns
    #last_position=rows
    if last_position==0:
        return numbers
    if current_pos<=len(numbers)-2:
        if numbers[current_pos]>numbers[max]:
            return selectsort(numbers,current_pos+1,last_position,max)
        else: 
            return selectsort(numbers,current_pos+1,last_position,max)
    else:  
        numbers[last_position-1],numbers[max]=numbers[max],numbers[last_position-1]
        return selectsort(numbers,last_position-1,0,0)
    


print(selectsort([4,5,6,1],0,3,0))