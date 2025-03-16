def bubble_sort(numbers_list):
    for idx_i, element_i in enumerate(numbers_list):
        print('\ni',idx_i, element_i, '\n')
        for idx_j, element_j in enumerate(numbers_list):
            print('j',idx_j, element_j)
            if element_i >= element_j:
                numbers_list[idx_i], numbers_list[idx_j] = numbers_list[element_j], numbers_list[element_i]
    return numbers_list


numbers_list = [3,0,1,2,6]
print(bubble_sort(numbers_list))