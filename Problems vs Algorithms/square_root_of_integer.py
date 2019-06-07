def sqrt(number):
    """
   Calculate the floored square root of a number

   Args:
   number(int): Number to find the floored squared root
   Returns:
   int: Floored Square Root
   """
    start_number = 1
    end_number = number // 2

    if number == 0 or number == 1:
        return number

    while start_number <= end_number:
        mid_number = (start_number + end_number) // 2
        if mid_number * mid_number == number:
            return mid_number
        elif mid_number * mid_number < number:
            start_number = mid_number + 1
            result = mid_number
        else:
            end_number = mid_number - 1

    return result


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
