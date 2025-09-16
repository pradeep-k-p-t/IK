def get_intersection_built_in(numbers1 : list[int], numbers2 : list[int])->list: 
    intersect =  list(set(numbers1).intersection(set(numbers2)))
    if len(intersect) == 0:
        return [-1]
    return intersect


print(get_intersection_built_in([1,2,3,4],[1,2,4,5,6]))