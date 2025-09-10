def is_contain_duplicate(nums : list[int]):
    # check if the list contain duplicate 
    if nums == None or len(nums) == 0: 
        return False
    else:
        ele_count = ()
        for i in nums: 
            if i in ele_count: 
                return True
            else: 
                ele_count.add(i)
    return False


