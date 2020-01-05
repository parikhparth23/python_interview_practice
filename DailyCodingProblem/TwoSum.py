def twoSum(nums, target):

    # index_map = {}
    # for i in range(len(nums)):
    #     num = nums[i]
    #     pair = target - num
    #     if pair in index_map:
    #         # return [index_map[pair], nums[i]]
    #         return [index_map[pair], i]
    #     # index_map[num] = nums[i]
    #     index_map[num] = i
    #
    # return None

    count = []

    for i in nums:
        tmp = target - i
        if tmp in count:
            print('Two values are: %d and %d.' % (i, tmp))
            return True
        else:
            count.append(i)
    return False


nums = [10, 15, 3, 7]
target = 17
print(twoSum(nums, target))
