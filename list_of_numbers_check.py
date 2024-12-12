def areElementsNumbers(list):
    new_list = []
    return len([new_list.append(i) for i in list if not str(i).isdigit()]) == 0

list_example_1 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '_*6']
list_example_2 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '_*']
list_example_3 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '1ab']
list_example_4 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88, '127uy48']
list_example_5 = [123, 5, 67, 78, 21, 0, 1, 13, 40, 88]
print(areElementsNumbers(list_example_5))


