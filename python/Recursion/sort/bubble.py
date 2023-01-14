def bubble(numbers,current_pos,last_position): #numbers is the array. If the array is in the parameter, it won't create a new object during each function call
    if last_position==0:
        return numbers
    if current_pos<=len(numbers)-2:
        if numbers[current_pos]>numbers[current_pos+1]:
            numbers[current_pos],numbers[current_pos+1]=numbers[current_pos+1],numbers[current_pos]
        return bubble(numbers,current_pos+1,last_position)
    else:  
        return bubble(numbers,0,last_position-1)
    


print(bubble([4,5,6,1],0,3))