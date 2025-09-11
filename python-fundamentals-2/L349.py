def get_intersection_built_in(num1 : list[int], num2 : list[int])->list: 
    num1 = set(num1)
    num2 = set(num2)

    return list(num1.intersection(num2))

    


print(get_intersection_built_in([1,2,3,4],[1,2,4,5,6]))