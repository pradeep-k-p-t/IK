
def generate_sorted_array_of_squares(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # O(n)
    if numbers == None or len(numbers) == 0: 
        return []
    for i in range(0,len(numbers)): 
        numbers[i] = numbers[i]*numbers[i] 
    numbers.sort()
    return  numbers


print(generate_sorted_array_of_squares([-9, -5, -2, 0, 3, 7]))