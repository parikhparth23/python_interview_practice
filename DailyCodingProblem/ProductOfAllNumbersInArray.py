# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def productExceptSelf(nums):
    length = len(nums)
    output = [1] * length

    prod = 1
    for i in range(length):
        output[i] *= prod
        prod *= nums[i]
        # print("left:", end="")
        # print(output, prod)

    prod = 1
    for i in range(length - 1, -1, -1):
        output[i] *= prod
        prod *= nums[i]
        # print("right:", end="")
        # print(output, prod)

    return output


nums = [1, 2, 3, 4, 5]
print(productExceptSelf(nums))