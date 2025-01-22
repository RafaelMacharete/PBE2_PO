def insetion_sort(numbers_list):
    number_list_count = 1
    
    while number_list_count <= len(numbers_list)-1:
        current_value = numbers_list[number_list_count]
        idx = number_list_count
        while idx > 0:
            if current_value <= numbers_list[idx-1]:
                numbers_list[idx-1], numbers_list[idx] = current_value, numbers_list[idx-1]
            idx -= 1
        number_list_count += 1
    
    return numbers_list
        
numbers_list = [5,1,6,-2,-1,7,6,0,2,4,3]
insertion_list_sorted = insetion_sort(numbers_list)
print(insertion_list_sorted)