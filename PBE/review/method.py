# Exercise 1:
def reverse_string(string):
    string_len = len(string)-1
    reversed_string = ''

    while string_len >= 0:
        reversed_string += string[string_len]
        string_len -= 1
    
    return reversed_string

string = 'subinoonibus'
reverse_string_result = reverse_string(string)
print(reverse_string_result)

# Exercise 2:
def count_chars(string):
    dict_chars = {}

    for idx in string:
        if idx not in dict_chars:
            dict_chars[idx] = 1
        else:
            dict_chars[idx] += 1
    return dict_chars

string = 'subinoonibus'
result_dict_chars = count_chars(string)

print(result_dict_chars)