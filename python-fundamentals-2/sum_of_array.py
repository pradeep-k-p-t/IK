def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    cpm_dic = {}
    #O(n) time complexity & O(n) space complexity 
    for i in range(len(numbers)):
        if numbers[i] in cpm_dic: 
            return [cpm_dic[numbers[i]],i]
        else:
            cpm_dic[target-numbers[i]] = i
    return [-1,-1]

def without_add_space_sorted_array(numbers, target):
    left = 0 
    right = len(numbers)-1
    # o(n) without additonal space 
    while left < right: 
        current_sum = numbers[left] + numbers[right]
        if current_sum == target: 
            return [left,right]
        elif current_sum < target:
            left +=1 
        else:
            right -=1
    return [-1,-1]

arr = [2,3,4,8,10,15]
target =19
print(pair_sum_sorted_array(arr,target))
print(without_add_space_sorted_array(arr,target))

