# TO DIVIDE PART OF ALGORITHM
def merge_sort(number_list):
    half_len_of_list = len(number_list) // 2

    if len(number_list) <= 1:
        return number_list

    left_part_list = number_list[:half_len_of_list]
    right_part_list = number_list[half_len_of_list:]


    left_list = merge_sort(left_part_list)
    right_list = merge_sort(right_part_list)

    return merge(left_list, right_list)

# TO CONQUER PART OF ALGORITHM
def merge(left_part_list, right_part_list):
    merged_sorted_list = []
    idx_i = idx_j = 0

    while idx_i < len(left_part_list) and idx_j < len(right_part_list):
        if left_part_list[idx_i] <= right_part_list[idx_j]:
            merged_sorted_list.append(left_part_list[idx_i])
            idx_i += 1
        else:
            merged_sorted_list.append(right_part_list[idx_j])
            idx_j += 1

    while len(left_part_list) > idx_i:
        merged_sorted_list.append(left_part_list[idx_i])
        idx_i += 1

    while len(right_part_list) > idx_j:
        merged_sorted_list.append(right_part_list[idx_j])
        idx_j += 1

    return merged_sorted_list

# TO SEARCH REFERENCE VALUE ON TO ARRAY
def binary_search(sorted_list, reference_value):
    half_len_of_list = len(sorted_list) // 2

    left_search_part = sorted_list[:half_len_of_list]
    right_search_part = sorted_list[half_len_of_list:]

    # left_search_part = binary_search(left_search_part, reference_value)
    # right_search_part = binary_search(right_search_part, reference_value)

    if 


number_list = [4,2,1,3,8,5,7,6,10,12,11,14,19,16,17,15]
merged_sorted_list = merge_sort(number_list)

print(binary_search(merged_sorted_list, 10))