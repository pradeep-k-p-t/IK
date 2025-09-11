
def find_maximum_sum_subarray(numbers):
        if not numbers:
            return 0

        curSum = maxSum = numbers[0]
        for num in numbers[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

test_list = [-10, 10000]

print(find_maximum_sum_subarray(test_list))


            
            
