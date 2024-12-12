def are_elements_numbers(initial_list):
    new_list = []
    return len([new_list.append(i) for i in initial_list if not str(i).isdigit()]) == 0

# Another solution that stops when non digit is found
def contains_only_numbers(initial_list):
    contain_only_digits = True
    for i in initial_list:
        if not str(i).isdigit():
            contain_only_digits = False
            break
    return contain_only_digits

list_example_1 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '_*6']
list_example_2 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '_*']
list_example_3 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '1ab']
list_example_4 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '127uy48']
list_example_5 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88]
list_example_6 = []
print(are_elements_numbers(list_example_3))
print(contains_only_numbers(list_example_3))

print(are_elements_numbers(list_example_5))
print(contains_only_numbers(list_example_5))