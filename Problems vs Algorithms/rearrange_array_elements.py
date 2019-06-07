def sort(input_list):
    if len(input_list) < 2:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    sorted_left = sort(left)
    sorted_right = sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = sort(input_list)

    dgt_1 = []
    dgt_2 = []

    for i, v in enumerate(sorted_input_list[::-1]):
        if i % 2 == 0:
            dgt_2.append(v)
        else:
            dgt_1.append(v)

    num_1 = int("".join(map(str, dgt_1)))
    num_2 = int("".join(map(str, dgt_2)))

    return [num_1, num_2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 7, 9, 8], [974, 862]])
