def is_contain_duplicate(nums : list[int]):
    # check if the list contain duplicate 
    if len(nums) > len(set(nums)):
        return True
    return False


