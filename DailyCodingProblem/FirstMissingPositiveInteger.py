# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


def firstMissingPositiveInteger(nums):
    nums.sort()
    # print("nums:", nums)
    length = len(nums)
    low = nums[0]
    # print("low:", low)
    high = nums[length-1]
    # print("high:", high)

    for i in range(low, high+1):
        # print("value of i:", i, end= " ")
        if i not in nums and i > 0:
            # print(i)
            return i
    # print(nums[length - 1] + 1)
    return nums[length - 1] + 1


print(firstMissingPositiveInteger([3, 4, -1, 1]))
# firstMissingPositiveInteger([3, 4, -1, 1])
# print(firstMissingPositiveInteger([1, 2, 0]))