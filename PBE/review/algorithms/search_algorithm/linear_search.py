def linear_search(numbers_list, reference_value):
    for idx in numbers_list:
        if idx == reference_value:
            return True
        else:
            return False
        

numbers_list = [1,2,3,4,8,7,6,5]
reference_value = 0

result_linear_search = linear_search(numbers_list, reference_value)
print(result_linear_search)