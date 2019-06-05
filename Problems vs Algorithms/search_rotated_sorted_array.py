def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def binary_search(start_index=0, end_index=len(input_list) - 1):
        mid_index = (start_index + end_index) // 2

        if start_index > end_index:
            return -1
        elif number == input_list[mid_index]:
            return mid_index
        elif number > input_list[mid_index]:
            if input_list[mid_index] < input_list[start_index] and number >= input_list[start_index]:
                return binary_search(start_index, mid_index - 1)
            else:
                return binary_search(mid_index + 1, end_index)
        else:
            if input_list[mid_index] > input_list[end_index] and number <= input_list[end_index]:
                return binary_search(mid_index + 1, end_index)
            else:
                return binary_search(start_index, mid_index - 1)

    result = binary_search()
    return result

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])